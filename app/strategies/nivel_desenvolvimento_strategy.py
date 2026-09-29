from app.strategies.quiz_strategy import QuizStrategy


class NivelDesenvolvimentoStrategy(QuizStrategy):

    def avaliar(self, percentual):

        return {
            "nivel": "Em Desenvolvimento",
            "titulo": "Ainda há pontos cegos.",
            "mensagem": (
                "Você tem uma base. Mas ainda existem "
                "pontos cegos — e eles custam caro."
            ),
            "cor": "#eab308"
        }