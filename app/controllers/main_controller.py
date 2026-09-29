from flask import Blueprint
from flask import render_template
from app.helpers.auth import login_required
from flask import request
from app.services.quiz_service import QuizService
from app.services.session_service import SessionService
from app.services.manifesto_service import ManifestoService
from app.services.simulador_service import (
    SimuladorService
)
from app.models.simulador import Simulador
from app.models.cenario_simulador import (
    CenarioSimulador
)

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():

    usuario = SessionService.usuario_logado()

    total_assinaturas = (
        ManifestoService.total_assinaturas()
    )

    return render_template(
        "index.html",
        usuario_logado=usuario.nome if usuario else None,
        total_assinaturas=total_assinaturas
    )
# Rotas protegidas por login - acessíveis apenas para usuários autenticados
@main_bp.route("/quiz")
@login_required
def quiz():

    perguntas = QuizService.buscar_perguntas()

    return render_template(
        "quiz.html",
        perguntas=perguntas
    )

@main_bp.route("/quiz/resultado", methods=["POST"])
@login_required
def quiz_resultado():

    dados = request.get_json()

    acertos = dados.get("acertos")

    total = QuizService.total_perguntas()

    resultado = QuizService.calcular_resultado(
        acertos,
        total
    )

    return render_template(
        "quiz-resultado.html",
        acertos=acertos,
        total=total,
        resultado=resultado
    )

@main_bp.route("/simulador")
@login_required
def simulador():

    cenarios = (
        CenarioSimulador.query.all()
    )

    cenarios_json = []

    for cenario in cenarios:

        opcoes = []

        for opcao in cenario.opcoes:

            opcoes.append({
                "texto": opcao.texto,
                "peso": opcao.peso,
                "estado": opcao.estado
            })

        cenarios_json.append({
            "id": cenario.id,
            "titulo": cenario.titulo,
            "contexto": cenario.contexto,
            "opcoes": opcoes
        })

    return render_template(
        "simulador.html",
        cenarios=cenarios_json
    )

    
@main_bp.route(
    "/simulador/resultado",
    methods=["POST"]
)
@login_required
def resultado_simulador():

    dados = request.get_json()

    pontuacao = dados.get("pontuacao")

    pontuacao_maxima = dados.get(
        "pontuacao_maxima"
    )

    resultado = SimuladorService.gerar_resultado(
        pontuacao,
        pontuacao_maxima
    )

    usuario = SessionService.usuario_logado()

    simulador = Simulador.query.first()

    ja_respondeu = SimuladorService.usuario_ja_respondeu(
        usuario.id,
        simulador.id
    )

    SimuladorService.salvar_resultado(
        pontuacao=pontuacao,
        estado_final=resultado["estado"],
        usuario_id=usuario.id,
        simulador_id=simulador.id,
        primeira_resposta=not ja_respondeu
    )

    estatistica_perfil = (
        SimuladorService.calcular_estatistica_por_estado(
            resultado["estado"]
        )
    )

    return render_template(
        "simulador-resultado.html",
        resultado=resultado,
        estatistica_omissao=estatistica_perfil
    )


# Rotas públicas - acessíveis para todos os visitantes, independentemente do login
@main_bp.route("/consequencias")
def consequencias():

    return render_template("consequencias.html")

@main_bp.route("/recursos_reflexao")
def recursos_reflexao():

    return render_template("recursos-reflexao.html")


@main_bp.route("/tipos_violencia")
def tipos_violencia():

    return render_template("tipos-violencia.html")

#Rotas para os tipos de violência - cada uma renderiza uma página específica para o tipo correspondente    

@main_bp.route("/violencia_digital")
def violencia_digital():

    return render_template("violencia-digital.html")

@main_bp.route("/violencia_fisica")
def violencia_fisica():

    return render_template("violencia-fisica.html")

@main_bp.route("/violencia_moral")
def violencia_moral():

    return render_template("violencia-moral.html")

@main_bp.route("/violencia_patrimonial")
def violencia_patrimonial():

    return render_template("violencia-patrimonial.html")

@main_bp.route("/violencia_psicologica")
def violencia_psicologica():

    return render_template("violencia-psicologica.html")

@main_bp.route("/violencia_sexual")
def violencia_sexual():

    return render_template("violencia-sexual.html")
