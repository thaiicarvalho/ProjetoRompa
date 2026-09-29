from app.database import db

from app.context.simulador_context import (
    SimuladorContext
)

from app.models.resultado_simulador import (
    ResultadoSimulador
)


class SimuladorService:

    @staticmethod
    def calcular_percentual(
        pontuacao,
        pontuacao_maxima
    ):

        return (
            pontuacao / pontuacao_maxima
        ) * 100

    @staticmethod
    def gerar_resultado(
        pontuacao,
        pontuacao_maxima
    ):

        percentual = (
            SimuladorService.calcular_percentual(
                pontuacao,
                pontuacao_maxima
            )
        )

        context = SimuladorContext(
            percentual
        )

        resultado = (
            context.gerar_resultado()
        )

        resultado["pontuacao"] = pontuacao

        return resultado

    @staticmethod
    def salvar_resultado(
        pontuacao,
        estado_final,
        usuario_id,
        simulador_id,
        primeira_resposta=True
    ):

        resultado = ResultadoSimulador(
            pontuacao=pontuacao,
            estado_final=estado_final,
            usuario_id=usuario_id,
            simulador_id=simulador_id,
            primeira_resposta=primeira_resposta
        )

        db.session.add(resultado)

        db.session.commit()

        return resultado

    @staticmethod
    def usuario_ja_respondeu(
        usuario_id,
        simulador_id
    ):

        resultado = (
            ResultadoSimulador.query.filter_by(
                usuario_id=usuario_id,
                simulador_id=simulador_id
            ).first()
        )

        return resultado is not None

    @staticmethod
    def calcular_estatistica_por_estado(estado_final):

        total = ResultadoSimulador.query.filter_by(
            primeira_resposta=True
        ).count()

        if total == 0:
            return 0

        total_mesmo_estado = ResultadoSimulador.query.filter_by(
            estado_final=estado_final,
            primeira_resposta=True
        ).count()

        percentual = (
            total_mesmo_estado / total
        ) * 100

        return round(percentual)