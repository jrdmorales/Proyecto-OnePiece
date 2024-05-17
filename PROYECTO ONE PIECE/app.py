from flask import Flask
from extensions import db
from routes.main import main_bp
from routes.personajes import personajes_bp
from routes.tripulaciones import tripulaciones_bp
from routes.tipos_frutas import tipos_frutas_bp
from routes.barcos import barcos_bp
from routes.islas import islas_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(personajes_bp, url_prefix='/personajes')
    app.register_blueprint(tripulaciones_bp, url_prefix='/tripulaciones')
    app.register_blueprint(tipos_frutas_bp, url_prefix='/tipos_frutas')
    app.register_blueprint(barcos_bp, url_prefix='/barcos')
    app.register_blueprint(islas_bp, url_prefix='/islas')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
