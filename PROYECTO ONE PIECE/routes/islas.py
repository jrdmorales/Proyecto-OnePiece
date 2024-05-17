from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db

islas_bp = Blueprint('islas', __name__)

@islas_bp.route('/')
def islas():
    islas = list(db.db.islas.find())
    return render_template('islas.html', islas=islas)

@islas_bp.route('/buscar')
def buscar_islas():
    nombre = request.args.get('search')
    islas = list(db.db.islas.find({
        '$or': [
            {'_id': {"$regex": nombre, "$options": "i"}},
            {'nombre': {"$regex": nombre, "$options": "i"}},
            {'localizacion': {"$regex": nombre, "$options": "i"}},
            {'habitantes': {"$regex": nombre, "$options": "i"}}
        ]
    }))
    return render_template('islas.html', islas=islas)

@islas_bp.route('/agregar', methods=['POST'])
def agregar_isla():
    total_documentos = db.db.islas.count_documents({})
    # Calcular el nuevo ID
    nuevo_id = total_documentos + 1
    # Insertar el nuevo documento con el nuevo ID
    db.db.islas.insert_one({
        '_id': nuevo_id,
        'nombre': request.form['nombre'],
        'localizacion': request.form['localizacion'],
        'habitantes': request.form['habitantes']
    })
    return redirect(url_for('islas.islas'))

@islas_bp.route('/eliminar', methods=['POST'])
def eliminar_isla():
    db.db.islas.delete_one({'nombre': request.form.get('nombre')})
    return redirect(url_for('islas.islas'))
