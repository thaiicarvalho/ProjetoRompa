from app.states.resultado_state import (
    ResultadoState
)


class PosturaAtivaState(ResultadoState):

    def gerar_resultado(self):

        return {
            "estado": "ATIVA",
            "titulo": (
                "Suas respostas mostram "
                "que o silêncio não é uma opção"
            ),
            "mensagem": (
                "Você demonstrou uma postura "
                "ativa e consciente diante "
                "de situações problemáticas."
            ),
            "cor": "#22c55e"
        }