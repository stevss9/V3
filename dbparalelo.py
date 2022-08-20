class Paralelo:
    def __init__(self, idparalelo, descripcion, estado):
        self.idparalelo = idparalelo
        self.descripcion = descripcion
        self.estado = estado


    def toDBCollection(self):
        return{
            '_id': self.idparalelo,
            'Descripcion': self.descripcion,
            'Estado': self.estado,
        }