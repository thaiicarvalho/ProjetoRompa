from app.database import db


class OpcaoSimulador(db.Model):

    __tablename__ = "opcoes_simulador"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    texto = db.Column(
        db.Text,
        nullable=False
    )

    peso = db.Column(
        db.Integer,
        nullable=False
    )

    estado = db.Column(
        db.String(50),
        nullable=False
    )

    cenario_id = db.Column(
        db.Integer,
        db.ForeignKey("cenarios_simulador.id"),
        nullable=False
    )