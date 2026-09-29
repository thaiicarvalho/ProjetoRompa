from app.database import db

class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    senha_hash = db.Column(
        db.String(255),
        nullable=False
    )

    manifestos = db.relationship(
        "Manifesto",
        backref="usuario",
        lazy=True
    )

    resultados_quiz = db.relationship(
        "ResultadoQuiz",
        backref="usuario",
        lazy=True
   )

    def __init__(self, nome, username, senha_hash):

        self.nome = nome
        self.username = username
        self.senha_hash = senha_hash

   