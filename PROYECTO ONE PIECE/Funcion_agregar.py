import os
from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from flask_pymongo import PyMongo
from pymongo import errors
from bson import json_util
from pymongo import MongoClient
from conexion import connect

##FUNCION PARA BUSCAR
db = connect()
app = Flask(__name__)
##FUNCION PARA AGREGAR
class Funcion_agregar:
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

    def agregar_tipo_fruta():
        nombre = request.form['nombre']
        db.tipos_frutas.insert_one({
            'nombre': nombre
        })
        return redirect(url_for('tipos_frutas'))

    def agregar_barco():
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        tripulacion_id = request.form['tripulacion_id']
        estado = request.form['estado']
        db.barcos.insert_one({
            'nombre': nombre,
            'tipo': tipo,
            'tripulacion_id': tripulacion_id,
            'estado': estado
        })
        return redirect(url_for('barcos'))

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