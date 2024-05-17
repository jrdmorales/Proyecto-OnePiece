from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db

tipos_frutas_bp = Blueprint('tipos_frutas', __name__)

@tipos_frutas_bp.route('/')
def tipos_frutas():
    tipos_frutas = list(db.db.tipos_frutas.find())
    return render_template('tipos_frutas.html', tipos_frutas=tipos_frutas)

@tipos_frutas_bp.route('/buscar')
def buscar_tipos_frutas():
    nombre = request.args.get('search')
    tipos_frutas = list(db.db.tipos_frutas.find({'nombre': {"$regex": nombre, "$options": "i"}}))
    return render_template('tipos_frutas.html', tipos_frutas=tipos_frutas)

@tipos_frutas_bp.route('/agregar', methods=['POST'])
def agregar_tipo_fruta():
    total_documentos = db.db.tipos_frutas.count_documents({})
    # Calcular el nuevo ID
    nuevo_id = total_documentos + 1
    # Insertar el nuevo documento con el nuevo ID
    db.db.tipos_frutas.insert_one({'_id': nuevo_id,
                                   'nombre': request.form['nombre']})
    return redirect(url_for('tipos_frutas.tipos_frutas'))

@tipos_frutas_bp.route('/eliminar', methods=['POST'])
def eliminar_tipo_fruta():
    db.db.tipos_frutas.delete_one({'nombre': request.form.get('nombre')})
    return redirect(url_for('tipos_frutas.tipos_frutas'))
