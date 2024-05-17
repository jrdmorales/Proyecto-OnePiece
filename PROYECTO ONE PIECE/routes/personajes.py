from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db

personajes_bp = Blueprint('personajes', __name__)

@personajes_bp.route('/')
def personajes():
    personajes = list(db.db.personajes.find())
    return render_template('personajes.html', personajes=personajes)

@personajes_bp.route('/buscar')
def buscar_personajes():
    nombre = request.args.get('search')
    personajes = list(db.db.personajes.find({
        '$or': [
            {'_id': {"$regex": nombre, "$options": "i"}},
            {'nombre': {"$regex": nombre, "$options": "i"}},
            {'rol': {"$regex": nombre, "$options": "i"}},
            {'fruta_del_diablo': {"$regex": nombre, "$options": "i"}},
            {'isla_natal': {"$regex": nombre, "$options": "i"}},
            {'tripulacion_id': {"$regex": nombre, "$options": "i"}},
            {'edad': {"$regex": nombre, "$options": "i"}},
            {'recompensa': {"$regex": nombre, "$options": "i"}}
        ]
    }))
    return render_template('personajes.html', personajes=personajes)

@personajes_bp.route('/agregar', methods=['POST'])
def agregar_personaje():
    total_documentos = db.db.personajes.count_documents({})
    # Calcular el nuevo ID
    nuevo_id = total_documentos + 1
    # Insertar el nuevo documento con el nuevo ID
    db.db.personajes.insert_one({
        '_id': nuevo_id,
        'nombre': request.form['nombre'],
        'rol': request.form['rol'],
        'fruta_del_diablo': request.form['fruta_del_diablo'],
        'isla_natal': request.form['isla_natal'],
        'tripulacion_id': request.form['tripulacion_id'],
        'edad': request.form['edad'],
        'recompensa': request.form['recompensa']
    })
    return redirect(url_for('personajes.personajes'))

@personajes_bp.route('/eliminar', methods=['POST'])
def eliminar_personaje():
    db.db.personajes.delete_one({'nombre': request.form.get('nombre')})
    return redirect(url_for('personajes.personajes'))
