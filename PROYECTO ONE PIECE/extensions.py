from flask_pymongo import PyMongo
from conexion import connect
class MongoDB:
    def __init__(self):
        self.db = None

    def init_app(self, app):
        app.config['MONGO_URI'] = "mongodb+srv://jordanmorales02:Jmorales4052.@cluster0.bcau67s.mongodb.net/one_piece?retryWrites=true&w=majority"
        self.db = connect()
        mongo = PyMongo(app)
        return mongo
    
    def get_db(self):
        return self.db
    

db= MongoDB()
