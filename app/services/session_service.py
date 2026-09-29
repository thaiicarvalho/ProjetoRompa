from flask import session

from app.models.usuario import Usuario


class SessionService:

    @staticmethod
    def usuario_logado():

        usuario_id = session.get("usuario_id")

        if not usuario_id:
            return None

        usuario = Usuario.query.get(usuario_id)

        return usuario

    @staticmethod
    def esta_logado():

        return "usuario_id" in session