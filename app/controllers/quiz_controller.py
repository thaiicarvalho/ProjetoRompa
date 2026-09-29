from flask import Blueprint
from flask import render_template
from flask import request
from flask import session

from app.decorators.login_required import (
    login_required
)

from app.models.quiz import Quiz

from app.services.quiz_service import QuizService


quiz_bp = Blueprint(
    "quiz",
    __name__
)


# =========================
# PÁGINA DO QUIZ
# =========================

@quiz_bp.route("/quiz")
@login_required
def quiz():

    return render_template(
        "quiz-resultado.html",
        resultado=resultado,
        acertos=acertos,
        total=total
   )


# =========================
# RESULTADO DO QUIZ
# =========================

@quiz_bp.route(
    "/quiz/resultado",
    methods=["POST"]
)
@login_required
def resultado():

    dados = request.get_json()

    acertos = int(
        dados.get("acertos", 0)
    )

    total = int(
        dados.get("total", 0)
    )

    usuario_id = session.get(
        "usuario_id"
    )

    quiz = Quiz.query.first()

    resultado = QuizService.avaliar_resultado(
        acertos,
        total
    )

    QuizService.salvar_resultado(
        pontuacao=acertos,
        nivel=resultado["nivel"],
        usuario_id=usuario_id,
        quiz_id=quiz.id
    )

    return render_template(
        "quiz-resultado.html",
        resultado=resultado,
        acertos=acertos,
        total=total
    )