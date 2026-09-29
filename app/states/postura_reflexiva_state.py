from app.states.resultado_state import (
    ResultadoState
)


class PosturaReflexivaState(ResultadoState):

    def gerar_resultado(self):

        return {
            "estado": "REFLEXIVA",
            "titulo": (
                "Você está no caminho da reflexão"
            ),
            "mensagem": (
                "Suas respostas mostram "
                "alguma consciência sobre "
                "essas situações, mas ainda "
                "existem pontos de hesitação."
            ),
            "cor": "#eab308"
        }