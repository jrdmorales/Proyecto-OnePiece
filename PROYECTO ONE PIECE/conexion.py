from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jordanmorales02:Jmorales4052.@cluster0.bcau67s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
def connect():
    client = MongoClient(uri, server_api=ServerApi('1')) 
    try:
        client.admin.command('ping')
        print("Conexión exitosa")
        db = client.one_piece
        return db
    except Exception as e:
        print("Error en la conexión a la base de datos:", e)


