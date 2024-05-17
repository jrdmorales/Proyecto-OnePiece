from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from bson import ObjectId

barcos_bp = Blueprint('barcos', __name__)

@barcos_bp.route('/')
def barcos():
    barcos = list(db.db.barcos.find())
    return render_template('barcos.html', barcos=barcos)

@barcos_bp.route('/buscar')
def buscar_barcos():
    nombre = request.args.get('search')
    barcos = list(db.db.barcos.find({
        '$or': [
            {'_id': {"$regex": nombre, "$options": "i"}},
            {'nombre': {"$regex": nombre, "$options": "i"}},
            {'tipo': {"$regex": nombre, "$options": "i"}},
            {'tripulacion_id': {"$regex": nombre, "$options": "i"}},
            {'estado': {"$regex": nombre, "$options": "i"}}
        ]
    }))
    return render_template('barcos.html', barcos=barcos)

@barcos_bp.route('/agregar', methods=['POST'])
def agregar_barco():
    db.db.barcos.insert_one({
        '_id': ObjectId(),
        'nombre': request.form['nombre'],
        'tipo': request.form['tipo'],
        'tripulacion_id': request.form['tripulacion_id'],
        'estado': request.form['estado']
    })
    return redirect(url_for('barcos.barcos'))

@barcos_bp.route('/eliminar', methods=['POST'])
def eliminar_barco():
    db.db.barcos.delete_one({'nombre': request.form.get('nombre')})
    return redirect(url_for('barcos.barcos'))
