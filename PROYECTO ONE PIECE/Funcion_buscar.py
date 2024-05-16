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

class Funcion_buscar:
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

    def buscar_tipos_frutas():
        nombre = request.args.get('search')
        tipos_frutas = list(db.tipos_frutas.find({'nombre': {"$regex": nombre, "$options": "i"}}))
        return render_template('tipos_frutas.html', tipos_frutas=tipos_frutas)

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

