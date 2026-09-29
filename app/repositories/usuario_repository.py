from app.models.usuario import Usuario
from app.database import db

class UsuarioRepository:

    @staticmethod
    def buscar_por_username(username):
        return Usuario.query.filter_by(username=username).first()

    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()