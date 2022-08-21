class Administrador:
    def toDBCollection(self):
        return{
            '_id': self.idestudiante,
            'Cedula': self.cedula,
            'Nombre1': self.name1,
            'Nombre2': self.name2,
            'Apellido1': self.lastname1,
            'Apellido2': self.lastname2,
            'Correo': self.correo,
            'Clave': self.Clave,
            'Telefono': self.telefono
        }