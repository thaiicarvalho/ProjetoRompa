from app.database import db

from app.models.resultado_quiz import ResultadoQuiz

from app.models.pergunta_quiz import PerguntaQuiz

from app.strategies.nivel_alerta_strategy import (
    NivelAlertaStrategy
)

from app.strategies.nivel_desenvolvimento_strategy import (
    NivelDesenvolvimentoStrategy
)

from app.strategies.nivel_consciente_strategy import (
    NivelConscienteStrategy
)


class QuizService:

    @staticmethod
    def buscar_perguntas():

        perguntas = PerguntaQuiz.query.all()

        return [
            {
            "id": pergunta.id,

            "scenario":
                pergunta.enunciado,

            "correctAnswer":
                pergunta.alternativa_correta,

            "correctLabel":
                pergunta.texto_alternativa_correta(),

            "options": [
                {
                    "id": "a",
                    "label":
                        pergunta.alternativa_a
                },

               {
                    "id": "b",
                    "label":
                        pergunta.alternativa_b
                },

               {
                    "id": "c",
                    "label":
                        pergunta.alternativa_c
               },

               {
                    "id": "d",
                    "label":
                        pergunta.alternativa_d
                }
            ],

            "explanation":
            pergunta.explicacao
    }

    for pergunta in perguntas
   
 ]

    @staticmethod
    def total_perguntas():

        return len(
            QuizService.buscar_perguntas()
        )

    @staticmethod
    def calcular_percentual(
        acertos,
        total_perguntas
    ):

        return (
            acertos / total_perguntas
        ) * 100

    @staticmethod
    def selecionar_strategy(percentual):

        if percentual >= 80:

            return NivelConscienteStrategy()

        elif percentual >= 50:

            return NivelDesenvolvimentoStrategy()

        return NivelAlertaStrategy()

    @staticmethod
    def avaliar_resultado(
        acertos,
        total_perguntas
    ):

        percentual = (
            QuizService.calcular_percentual(
                acertos,
                total_perguntas
            )
        )

        strategy = (
            QuizService.selecionar_strategy(
                percentual
            )
        )

        resultado = strategy.avaliar(
            percentual
        )

        resultado["percentual"] = percentual

        return resultado
    

    @staticmethod
    def calcular_resultado(acertos, total_perguntas):

        return QuizService.avaliar_resultado(acertos,total_perguntas)


    @staticmethod
    def salvar_resultado(
        pontuacao,
        nivel,
        usuario_id,
        quiz_id
    ):

        resultado = ResultadoQuiz(
            pontuacao=pontuacao,
            nivel=nivel,
            usuario_id=usuario_id,
            quiz_id=quiz_id
        )

        db.session.add(resultado)

        db.session.commit()

        return resultado