from app.database import db

from app.models.manifesto import Manifesto


class ManifestoService:

    @staticmethod
    def usuario_ja_assinou(usuario_id):

        assinatura = Manifesto.query.filter_by(
            usuario_id=usuario_id
        ).first()

        return assinatura is not None

    @staticmethod
    def assinar(usuario_id):

        if ManifestoService.usuario_ja_assinou(usuario_id):
            return False

        manifesto = Manifesto(
            usuario_id=usuario_id
        )

        db.session.add(manifesto)

        db.session.commit()

        return True

    @staticmethod
    def total_assinaturas():

        return Manifesto.query.count()