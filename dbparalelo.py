class Paralelo:
    def __init__(self, idparalelo, descripcion, estado):
        """
     función  _init_
    
    Parameters
    ------------
    llamamos a nuestros name del formulario para el administrador

     Return
     -----------
    
    """
        self.idparalelo = idparalelo
        self.descripcion = descripcion
        self.estado = estado

    """
     función  toDBCollection con parámetro self
    
    Parameters
    ------------
  
     Return
     -----------
      devuelve la estructura de la coelccion paralelo y llamamos con el name a nuestros campos

    
    """
    def toDBCollection(self):
        return{
            '_id': self.idparalelo,
            'Descripcion': self.descripcion,
            'Estado': self.estado,
        }