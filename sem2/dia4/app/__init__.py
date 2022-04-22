from flask import Flask

#importamos Blueprints
from .admin import admin
from .portafolio import portafolio

#importamos config
from .config import Config

def create_app():
    app = Flask(__name__)

    # Agregamos el Blueprint al proyecto principal
    app.register_blueprint(admin)
    app.register_blueprint(portafolio)
    
    return app


