
#creamos clase administrador
class Administrador:
    def __init__(self, idadministrador,cedula, name1, name2,lastname1, lastname2, mail, pwd, cell):
        """
     función  _init_
    
    Parameters
    ------------
    llamamos a nuestros name del formulario para el administrador

     Return
     -----------
    
    """
        self.idadministrador = idadministrador
        self.cedula = cedula
        self.name1 = name1
        self.name2 = name2
        self.lastname1 = lastname1
        self.lastname2 = lastname2       
        self.mail = mail
        self.pwd = pwd
        self.cell = cell

    def toDBCollection(self):
        """
     función  toDBCollection con parámetro self
    
    Parameters
    ------------
   asignamos la estructura de la coelccion personas y llamamos con el name a nuestros campos

     Return
     -----------
    
    """
        return{
            '_id': self.iddocente,
            'Cedula': self.cedula,
            'Nombre1': self.name,
            'Nombre2': self.lastname,
            'Apellido1': self.rol,
            'Apellido2': self.alectivo,
            'Correo': self.mail,
            'Contraseña': self.pwd,
            'Telefono': self.cell
        }