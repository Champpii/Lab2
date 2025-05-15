from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_config import FlaskConfig
from routes.routes_clientes import clientes_bp
from routes.routes_asuntos import asuntos_bp
from routes.routes_gabinete import gabinetes_bp

class AppInitializer:
    def __init__(self):
        """Inicializa la aplicación Flask y configura extensiones."""
        self.app = Flask(__name__)
        self.configure_app()
        self.register_routes()
    
    def configure_app(self):
        """Configura la aplicación Flask con parámetros generales."""
        self.app.config.from_object(FlaskConfig)
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)
        CORS(self.app)  # Habilita soporte para CORS si es necesario
    
    def register_routes(self):
        """Registra todos los Blueprints (rutas) en Flask."""
        self.app.register_blueprint(clientes_bp, url_prefix="/api")
        self.app.register_blueprint(asuntos_bp, url_prefix="/api")
        self.app.register_blueprint(gabinetes_bp, url_prefix="/api")

    def get_app(self):
        """Retorna la instancia de la aplicación Flask."""
        return self.app
