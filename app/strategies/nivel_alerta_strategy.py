from app.strategies.quiz_strategy import QuizStrategy


class NivelAlertaStrategy(QuizStrategy):

    def avaliar(self, percentual):

        return {
            "nivel": "Alerta",
            "titulo": "O que você não vê, dói em alguém.",
            "mensagem": (
                "O silêncio começa quando não reconhecemos. "
                "Explore cada tipo com atenção."
            ),
            "cor": "#ef4444"
        }