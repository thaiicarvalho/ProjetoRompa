from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

# =========================
# CADASTRO
# =========================

@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "GET":
        return render_template("cadastro.html")

    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    username = request.form.get("username")
    password = request.form.get("password")

    nome_completo = f"{first_name} {last_name}"

    sucesso, mensagem = AuthService.cadastrar(
        nome_completo,
        username,
        password
    )

    if not sucesso:
        return render_template(
            "cadastro.html",
            erro=mensagem
        )

    return redirect(url_for("auth.login"))

# =========================
# LOGIN
# =========================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    usuario, mensagem = AuthService.autenticar(username,password)

    if not usuario:
        return render_template(
            "login.html",
            erro=mensagem
       )

    session["usuario_id"] = usuario.id
    session["usuario_nome"] = usuario.nome

    return redirect(url_for("main.index"))

# =========================
# LOGOUT
# =========================

@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("main.index"))

@auth_bp.route("/cadastro-aviso")
def cadastro_aviso():

    return render_template("cadastro-aviso.html")    

