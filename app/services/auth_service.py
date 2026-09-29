from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository

class AuthService:

    @staticmethod
    def cadastrar(nome, username, senha):

        usuario_existente = UsuarioRepository.buscar_por_username(username)

        if usuario_existente:
            return False, "Usuário já existe"

        senha_hash = generate_password_hash(senha)

        usuario = Usuario(
            nome,
            username,
            senha_hash
        )

        UsuarioRepository.salvar(usuario)

        return True, "Usuário cadastrado com sucesso"

    @staticmethod
    def autenticar(username, senha):

        usuario = UsuarioRepository.buscar_por_username(username)

        if not usuario:
            return None, "Usuário não encontrado"

        senha_correta = check_password_hash(usuario.senha_hash, senha)

        if not senha_correta:
           return None, "Usuário ou senha incorretos"

        return usuario, "Login realizado com sucesso"