from app.database import db


class Simulador(db.Model):

    __tablename__ = "simuladores"

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

    cenarios = db.relationship(
        "CenarioSimulador",
        backref="simulador",
        lazy=True
    )

    resultados = db.relationship(
        "ResultadoSimulador",
        backref="simulador",
        lazy=True
    )