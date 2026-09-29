from app import db
from datetime import datetime


class Manifesto(db.Model):

    __tablename__ = "manifestos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    data_assinatura = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )