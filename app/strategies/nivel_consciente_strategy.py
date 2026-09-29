from app.strategies.quiz_strategy import QuizStrategy


class NivelConscienteStrategy(QuizStrategy):

    def avaliar(self, percentual):

        return {
            "nivel": "Consciente",
            "titulo": "Você enxerga.",
            "mensagem": (
                "Você reconhece. Agora é hora de agir "
                "e fazer outros reconhecerem também."
            ),
            "cor": "#22c55e"
        }