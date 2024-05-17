from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db

tripulaciones_bp = Blueprint('tripulaciones', __name__)

@tripulaciones_bp.route('/')
def tripulaciones():
    tripulaciones = list(db.db.tripulaciones.find())
    return render_template('tripulaciones.html', tripulaciones=tripulaciones)

@tripulaciones_bp.route('/buscar')
def buscar_tripulaciones():
    nombre = request.args.get('search')
    tripulaciones = list(db.db.tripulaciones.find({
        '$or': [
            {'_id': {"$regex": nombre, "$options": "i"}},
            {'nombre': {"$regex": nombre, "$options": "i"}},
            {'capitan_id': {"$regex": nombre, "$options": "i"}},
            {'numero_de_integrantes': {"$regex": nombre, "$options": "i"}},
            {'localizacion_actual': {"$regex": nombre, "$options": "i"}}
        ]
    }))
    return render_template('tripulaciones.html', tripulaciones=tripulaciones)

@tripulaciones_bp.route('/agregar', methods=['POST'])
def agregar_tripulacion():
    # Obtener el número total de documentos
    total_documentos = db.db.tripulaciones.count_documents({})
    # Calcular el nuevo ID
    nuevo_id = total_documentos + 1
    # Insertar el nuevo documento con el nuevo ID
    db.db.tripulaciones.insert_one({
        '_id': nuevo_id,
        'nombre': request.form['nombre'],
        'capitan_id': request.form['capitan_id'],
        'numero_de_integrantes': request.form['numero_de_integrantes'],
        'localizacion_actual': request.form['localizacion_actual']
    })
    return redirect(url_for('tripulaciones.tripulaciones'))


@tripulaciones_bp.route('/eliminar', methods=['POST'])
def eliminar_tripulacion():
    db.db.tripulaciones.delete_one({'nombre': request.form.get('nombre')})
    return redirect(url_for('tripulaciones.tripulaciones'))
