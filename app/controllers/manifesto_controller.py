from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from app.models.usuario import Usuario
from app.decorators.login_required import login_required
from app.services.manifesto_service import ManifestoService


manifesto_bp = Blueprint(
    "manifesto",
    __name__
)


# =========================
# PÁGINA DO MANIFESTO
# =========================

@manifesto_bp.route("/manifesto")
@login_required
def manifesto():


    usuario_id = session.get("usuario_id")

    print("USUARIO_ID:", usuario_id)

    usuario = Usuario.query.get(usuario_id)


    print("USUARIO:", usuario)


    usuario_nome = usuario.nome

    print("USUARIO_NOME:", usuario_nome)

    ja_assinou = ManifestoService.usuario_ja_assinou(
        usuario_id
    )

    total_assinaturas = ManifestoService.total_assinaturas()

    return render_template(
        "manifesto.html",
        usuario_logado=usuario_nome,
        ja_assinou=ja_assinou,
        total_assinaturas=total_assinaturas
    )


# =========================
# ASSINAR MANIFESTO
# =========================

@manifesto_bp.route("/manifesto/assinar", methods=["POST"])
@login_required
def assinar_manifesto():

    usuario_id = session.get("usuario_id")

    assinou = ManifestoService.assinar(
        usuario_id
    )

    if not assinou:

        return redirect(
            url_for("manifesto.manifesto")
        )

    return redirect(
        url_for("manifesto.sucesso")
    )


# =========================
# PÁGINA DE SUCESSO
# =========================

@manifesto_bp.route("/manifesto/sucesso")
@login_required
def sucesso():

    usuario_id = session.get("usuario_id")

    usuario = Usuario.query.get(usuario_id)

    usuario_nome = usuario.nome

    total_assinaturas = (
        ManifestoService.total_assinaturas()
    )

    return render_template(
        "manifesto-sucesso.html",
        usuario_logado=usuario_nome,
        total_assinaturas=total_assinaturas
    )