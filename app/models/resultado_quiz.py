from app.database import db


class ResultadoQuiz(db.Model):

    __tablename__ = "resultados_quiz"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pontuacao = db.Column(
        db.Integer,
        nullable=False
    )

    nivel = db.Column(
        db.String(50),
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    quiz_id = db.Column(
        db.Integer,
        db.ForeignKey("quizzes.id"),
        nullable=False
    )

    def __init__(
        self,
        pontuacao,
        nivel,
        usuario_id,
        quiz_id
    ):

        self.pontuacao = pontuacao
        self.nivel = nivel
        self.usuario_id = usuario_id
        self.quiz_id = quiz_id