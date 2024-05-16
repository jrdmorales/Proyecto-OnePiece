from flask import Flask, render_template, request, redirect, url_for,jsonify
from bson import ObjectId 
from flask_pymongo import PyMongo
from conexion import connect
from pymongo import  errors
from bson import json_util

app = Flask(__name__)
db = connect()

@app.route('/')
def home():
    personajes = list(db.personajes.find())
    tripulaciones = list(db.tripulaciones.find())
    tipos_frutas = list(db.tipos_frutas.find())
    barcos = list(db.barcos.find())
    islas = list(db.islas.find())
    return render_template('index.html', personajes=personajes, tripulaciones=tripulaciones, tipos_frutas=tipos_frutas, barcos=barcos, islas=islas)

@app.route('/personajes')
def personajes():
    personajes = list(db.personajes.find())
    return render_template('personajes.html', personajes=personajes)

@app.route('/tripulaciones')
def tripulaciones():
    tripulaciones = list(db.tripulaciones.find())
    return render_template('tripulaciones.html', tripulaciones=tripulaciones)

@app.route('/tipos_frutas')
def tipos_frutas():
    tipos_frutas = list(db.tipos_frutas.find())
    return render_template('tipos_frutas.html', tipos_frutas=tipos_frutas)

@app.route('/barcos')
def barcos():
    barcos = list(db.barcos.find())
    return render_template('barcos.html', barcos=barcos)

@app.route('/islas')
def islas():
    islas = list(db.islas.find())
    return render_template('islas.html', islas=islas)








##FUNCION PARA BUSCAR
@app.route('/buscar_personajes')
def buscar_personajes():
    nombre = request.args.get('search')
    personajes = list(db.personajes.find({
            '$or':[
                        {'_id': {"$regex": nombre, "$options": "i"}},
                      {'nombre': {"$regex": nombre, "$options": "i"}}, 
                      {'rol': {"$regex": nombre, "$options": "i"}},
                      {'fruta_del_diablo': {"$regex": nombre, "$options": "i"}},
                      {'isla_natal': {"$regex": nombre, "$options": "i"}},
                      {'tripulacion_id': {"$regex": nombre, "$options": "i"}},
                      {'edad': {"$regex": nombre, "$options": "i"}},
                      {'recompensa': {"$regex": nombre, "$options": "i"}}
                      ]}))
    return render_template('personajes.html', personajes=personajes)

@app.route('/buscar_tripulaciones')
def buscar_tripulaciones():
    nombre = request.args.get('search')
    tripulaciones = list(db.personajes.find({
            '$or':[
                      {'_id': {"$regex": nombre, "$options": "i"}},
                      {'nombre': {"$regex": nombre, "$options": "i"}}, 
                      {'capitan_id': {"$regex": nombre, "$options": "i"}},
                      {'numero_de_integrantes': {"$regex": nombre, "$options": "i"}},
                      {'localizacion_actual': {"$regex": nombre, "$options": "i"}}
                      ]}))
    return render_template('tripulaciones.html', tripulaciones=tripulaciones)

@app.route('/buscar_tipos_frutas')
def buscar_tipos_frutas():
    nombre = request.args.get('search')
    tipos_frutas = list(db.tipos_frutas.find({'nombre': {"$regex": nombre, "$options": "i"}}))
    return render_template('tipos_frutas.html', tipos_frutas=tipos_frutas)

@app.route('/buscar_barcos')
def buscar_barcos():
    nombre = request.args.get('search')
    barcos = list(db.barcos.find({
            '$or':[
                      {'_id': {"$regex": nombre, "$options": "i"}},
                      {'nombre': {"$regex": nombre, "$options": "i"}}, 
                      {'tipo': {"$regex": nombre, "$options": "i"}},
                      {'tripulacion_id': {"$regex": nombre, "$options": "i"}},
                      {'estado': {"$regex": nombre, "$options": "i"}}
                      ]}))
    return render_template('barcos.html', barcos=barcos)

@app.route('/buscar_islas')
def buscar_islas():
    nombre = request.args.get('search')
    islas = list(db.islas.find({
            '$or':[
                      {'_id': {"$regex": nombre, "$options": "i"}},
                      {'nombre': {"$regex": nombre, "$options": "i"}}, 
                      {'localizacion': {"$regex": nombre, "$options": "i"}},
                      {'habitantes': {"$regex": nombre, "$options": "i"}}
                      ]}))
    return render_template('islas.html', islas=islas)





##FUNCION PARA AGREGAR
@app.route('/agregar_personaje', methods=['POST'])
def agregar_personaje():
    nombre = request.form['nombre']
    rol = request.form['rol']
    fruta_del_diablo = request.form['fruta_del_diablo']
    isla_natal = request.form['isla_natal']
    tripulacion_id = request.form['tripulacion_id']
    edad = request.form['edad']
    recompensa = request.form['recompensa']
    db.personajes.insert_one({
        'nombre': nombre,
        'rol': rol,
        'fruta_del_diablo': fruta_del_diablo,
        'isla_natal': isla_natal,
        'tripulacion_id': tripulacion_id,
        'edad': edad,
        'recompensa': recompensa
    })
    return redirect(url_for('personajes'))

@app.route('/agregar_tripulacion', methods=['POST'])
def agregar_tripulacion():
    nombre = request.form['nombre']
    capitan_id = request.form['capitan_id']
    numero_de_integrantes = request.form['numero_de_integrantes']
    localizacion_actual = request.form['localizacion_actual']
    db.tripulaciones.insert_one({
        'nombre': nombre,
        'capitan_id': capitan_id,
        'numero_de_integrantes': numero_de_integrantes,
        'localizacion_actual': localizacion_actual
    })
    return redirect(url_for('tripulaciones'))

@app.route('/agregar_tipo_fruta', methods=['POST'])
def agregar_tipo_fruta():
    nombre = request.form['nombre']
    db.tipos_frutas.insert_one({
        'nombre': nombre
    })
    return redirect(url_for('tipos_frutas'))

@app.route('/agregar_barco', methods=['POST'])
def agregar_barco():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        tipo = request.form.get('tipo')
        tripulacion_id = request.form.get('tripulacion_id')
        estado = request.form.get('estado')
        if nombre and tipo and tripulacion_id and estado:
            # Genera un nuevo ID compuesto
            new_id = ObjectId()
            db.barcos.insert_one({
                '_id': new_id,
                'nombre': nombre,
                'tipo': tipo,
                'tripulacion_id': tripulacion_id,
                'estado': estado
            })
    return redirect(url_for('barcos'))


@app.route('/agregar_isla', methods=['POST'])
def agregar_isla():
    nombre = request.form['nombre']
    localizacion = request.form['localizacion']
    habitantes = request.form['habitantes']
    db.islas.insert_one({
        'nombre': nombre,
        'localizacion': localizacion,
        'habitantes': habitantes
    })
    return redirect(url_for('islas'))

##FUNCION PARA ELIMINAR
@app.route('/eliminar_personaje', methods=['POST'])
def eliminar_personaje():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        db.personajes.delete_one({'nombre': nombre})
        return redirect(url_for('personajes'))
    


@app.route('/eliminar_tripulacion', methods=['POST'])
def eliminar_tripulacion():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        db.tripulaciones.delete_one({'nombre': nombre})
        return redirect(url_for('tripulaciones'))
    
    

@app.route('/eliminar_barco', methods=['POST'])
def eliminar_barco():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        db.barcos.delete_one({'nombre': nombre})
        return redirect(url_for('barcos'))


@app.route('/eliminar_isla', methods=['POST'])
def eliminar_isla():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        db.islas.delete_one({'nombre': nombre})
        return redirect(url_for('islas'))
    
@app.route('/eliminar_tipo_fruta', methods=['POST'])
def eliminar_tipo_fruta():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        db.tipos_frutas.delete_one({'nombre': nombre})
        return redirect(url_for('tipos_frutas'))



if __name__ == '__main__':
    app.run(debug=True)