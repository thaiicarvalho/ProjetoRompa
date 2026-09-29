from app.database import db

from datetime import datetime


class ResultadoSimulador(db.Model):

    __tablename__ = "resultados_simulador"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pontuacao = db.Column(
        db.Integer,
        nullable=False
    )

    estado_final = db.Column(
        db.String(50),
        nullable=False
    )

    primeira_resposta = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    simulador_id = db.Column(
        db.Integer,
        db.ForeignKey("simuladores.id"),
        nullable=False
    )