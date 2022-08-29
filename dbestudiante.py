class Estudiante:
    def __init__(self, idestudiante,cedula, name,lastname, rol, alectivo, paralelo, estado, edad):
        """
     función  _init_
    
    Parameters
    ------------
    llamamos a nuestros name del formulario para el administrador

     Return
     -----------
    
    """
        self.idestudiante = idestudiante
        self.cedula = cedula
        self.name = name
        self.lastname = lastname
        self.rol = rol
        self.alectivo = alectivo
        self.paralelo = paralelo
        self.estado = estado
        self.edad = edad


    def toDBCollection(self):
        """
     función  toDBCollection con parámetro self
    
    Parameters
    ------------
  
     Return
     -----------
      devuelve la estructura de la coelccion personas y llamamos con el name a nuestros campos

    
    """
        return{
            '_id': self.idestudiante,
            'Cedula': self.cedula,
            'Nombre': self.name,
            'Apellido': self.lastname,
            'Rol': self.rol,
            'AñoLectivo': self.alectivo,
            'Paralelo': self.paralelo,
            'Estado': self.estado,
            'Edad': self.edad,
            'Nota': "0",
            'Entrenamiento': "0"
        }