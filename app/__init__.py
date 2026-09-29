from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app.database import db
from app.models.usuario import Usuario
from app.models.manifesto import Manifesto
from app.models.quiz import Quiz
from app.models.pergunta_quiz import PerguntaQuiz
from app.models.resultado_quiz import ResultadoQuiz
from app.models.simulador import Simulador
from app.models.cenario_simulador import (
    CenarioSimulador
)
from app.models.opcao_simulador import (
    OpcaoSimulador
)
from app.models.resultado_simulador import (
    ResultadoSimulador
)
from app.controllers.manifesto_controller import manifesto_bp
from app.controllers.quiz_controller import quiz_bp
from app.controllers.main_controller import main_bp
from app.controllers.auth_controller import auth_bp

migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(manifesto_bp)
    app.register_blueprint(quiz_bp)

#   print(app.url_map)

    return app