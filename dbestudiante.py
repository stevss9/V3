class Estudiante:
    def __init__(self, idestudiante,cedula, name,lastname, rol, alectivo, paralelo, estado, edad):
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