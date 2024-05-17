from flask import Blueprint, render_template
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    database = db.db
    context = {
        'personajes': list(database.personajes.find()),
        'tripulaciones': list(database.tripulaciones.find()),
        'tipos_frutas': list(database.tipos_frutas.find()),
        'barcos': list(database.barcos.find()),
        'islas': list(database.islas.find())
    }
    return render_template('index.html', **context)
