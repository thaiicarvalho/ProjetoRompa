from app.states.resultado_state import (
    ResultadoState
)


class PosturaOmissaState(ResultadoState):

    def gerar_resultado(self):

        return {
            "estado": "OMISSA",
            "titulo": (
                "O silêncio pode ser cumplicidade"
            ),
            "mensagem": (
                "Suas respostas indicam "
                "uma tendência à omissão "
                "diante de situações "
                "de violência e machismo."
            ),
            "cor": "#ef4444"
        }