#importamos MongoClient
from pymongo import MongoClient

#url de nuestro mongodb local
MONGO_URI = 'mongodb://localhost:27017'

def dbConnection():
    """
     función  dbConnection conectar con la base de datos
    
    Parameters
    ------------
    try
    client llamamos a nuestro MongoClient a la url
    db es igual a la base de datos DATABASE_ESCUELA
    EXCEPT en caso de que exista error mensaje de error
     Return
     -----------
     devuelve la base de datos
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client["DATABASE_ESCUELA"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
