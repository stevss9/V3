class Docente:
    def __init__(self, iddocente,cedula, name,lastname, rol, alectivo, paralelo, estado, mail, pwd):
        """
     función  _init_
    
    Parameters
    ------------
    llamamos a nuestros name del formulario para el administrador

     Return
     -----------
    
    """
        self.iddocente = iddocente
        self.cedula = cedula
        self.name = name
        self.lastname = lastname
        self.rol = rol
        self.alectivo = alectivo
        self.paralelo = paralelo
        self.estado = estado
        self.mail = mail
        self.pwd = pwd

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
            '_id': self.iddocente,
            'Cedula': self.cedula,
            'Nombre': self.name,
            'Apellido': self.lastname,
            'Rol': self.rol,
            'AñoLectivo': self.alectivo,
            'Paralelo': self.paralelo,
            'Estado': self.estado,
            'Correo': self.mail,
            'Contraseña': self.pwd
        }