from app.database import db


class Quiz(db.Model):

    __tablename__ = "quizzes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(150),
        nullable=False
    )

    descricao = db.Column(
        db.Text,
        nullable=False
    )

    perguntas = db.relationship(
        "PerguntaQuiz",
        backref="quiz",
        lazy=True
    )

    resultados = db.relationship(
        "ResultadoQuiz",
        backref="quiz",
        lazy=True
    )

    def __init__(self, titulo, descricao):

        self.titulo = titulo
        self.descricao = descricao