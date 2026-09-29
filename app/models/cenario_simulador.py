from app.database import db


class CenarioSimulador(db.Model):

    __tablename__ = "cenarios_simulador"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(150),
        nullable=False
    )

    contexto = db.Column(
        db.Text,
        nullable=False
    )

    simulador_id = db.Column(
        db.Integer,
        db.ForeignKey("simuladores.id"),
        nullable=False
    )

    opcoes = db.relationship(
        "OpcaoSimulador",
        backref="cenario",
        lazy=True
    )