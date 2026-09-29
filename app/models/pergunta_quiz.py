from app.database import db


class PerguntaQuiz(db.Model):

    __tablename__ = "perguntas_quiz"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    enunciado = db.Column(
        db.Text,
        nullable=False
    )

    alternativa_a = db.Column(
        db.String(255),
        nullable=False
    )

    alternativa_b = db.Column(
        db.String(255),
        nullable=False
    )

    alternativa_c = db.Column(
        db.String(255),
        nullable=False
    )

    alternativa_d = db.Column(
        db.String(255),
        nullable=False
    )

    alternativa_correta = db.Column(
        db.String(1),
        nullable=False
    )

    explicacao = db.Column(
        db.Text,
        nullable=False
    )

    quiz_id = db.Column(
        db.Integer,
        db.ForeignKey("quizzes.id"),
        nullable=False
    )

    def texto_alternativa_correta(self):

        alternativas = {

            "a": self.alternativa_a,

            "b": self.alternativa_b,

            "c": self.alternativa_c,

            "d": self.alternativa_d

        }

        texto = alternativas.get(
            self.alternativa_correta
      )

        if texto.startswith("Violência "):

            texto = texto.replace("Violência ","")

        return texto