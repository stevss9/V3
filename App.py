from flask import Flask, render_template, request, Response, jsonify, redirect, url_for, flash, session
import pymongo
import os

#importamos la clase de la conexion con la base de datos
import database as dbase 
#llamamos a nuestra clase estudiante
from dbestudiante import Estudiante
#llamamos a nuestra clase docente
from dbdocente import Docente 
#llamamos a nuestra clase paralelo
from dbparalelo import Paralelo
#llamamos a nuestra clase administrador
from dbadministrador import Administrador

#conexion a la base de datos

db = dbase.dbConnection()
#llamamos a la coleccion personas
usuarios = db['personas']
estudiantes = db['personas']
administador = db['administador']
personas = db['personas']
##coleccion paralelo
paralelo = db['paralelo']
administrador = db['administrador']
#coleccion aniolectivo
aniolectivo = db['aniolectivo']
rol = db['rol']

#inicializamos 
app = Flask(__name__) 
app._static_folder = os.path.abspath("static/")

#Controlador de la ruta inicial
@app.route('/')
def principal():
    """
     función index con 
    
     Parameters
        ------------

     Return
     -----------
     devuelve la subpage principalmain que se encuetra en la carpeta template
    """
    return render_template('principalmain.html')
#Controlador del login
@app.route('/login')
def login():
    """
     función login con 
    
     Parameters
        ------------

     Return
     -----------
     devuelve la subpage login que se encuetra en la carpeta template
    """
    return render_template('login.html')

#login admin
#Controlador de la ruta para borrar los datos de la tabla
@app.route('/login', methods=['POST'])
#Crea la funcion para el ingreso del login de administrador
def login1():
    """
     función login con método POST 
    
     Parameters
        ------------
    variable user que verifica que el correo sea distinto
    if redirige a login
    else que tiene la variable password que es igual al correo
    passw coje del formuario la contraseña
    if si es igual la contraseña redirige a la interfaz de docente
     Return
     -----------
     devuelve la subpage login que se encuetra en la carpeta template
    """
    #usuarios = db['personas']
    user = usuarios.distinct("Correo")
    if user is None:
        return render_template('login.html')
    else:
        password = user["Contraseña"]
        passw = request.form["password"]
        if user:
            if password == passw:
                return redirect(url_for('interfacedocente'))
        return render_template('login.html')

#decorador de login niños
@app.route('/loginn')
def loginn():
    """
     función login niños
    
     Parameters
        ------------
    variable estudiantesReceives donde hacemos una consulta de todos los estudiantes
    variable personasReceived donde hacemos una consulta de sólo estudiantes
     Return
     -----------
     devuelve la subpage login que se encuetra en la carpeta template y la busqueda de sólo estudiantes
    """
    #estudiantes = db['estudiantes']
    estudiantesReceived = estudiantes.find()
    personasReceived = personas.find({"Rol":"Estudiante"})
    return render_template('loginn.html', estudiantes = estudiantesReceived, personas = personasReceived)


#decorador traingame
@app.route('/traingame')
def traingame():

    """
     función traingame
    
     Parameters
    ------------
     Return
     -----------
     devuelve la subpage traingame que se encuetra en la carpeta template 
    """
    return render_template('traingame.html')


#decorador de subpage menugame
@app.route('/menugame')
def menugame():
    """
     función menugame
    
     Parameters
        ------------

     Return
     -----------
     devuelve la subpage menugame que se encuetra en la carpeta template
    """
    return render_template('menugame.html')


#decorador de evaluationgame
@app.route('/evaluationgame')
def evaluationgame():
    """
     función login evaluationfame
    
     Parameters
        ------------

     Return
     -----------
     devuelve la subpage  evaluationgame que se encuetra en la carpeta template
    """
    return render_template('evaluationgame.html')


#decorador de interfaz docente
@app.route('/interfacedocente')
def interfacedocente():
    """
     función interfaz docente
    
    Parameters
    ------------
    variable personasReceived donde hacemos una consulta a nuestra base de datos 
    sólo los de rol docente y paralelo z
     Return
     -----------
     devuelve la subpage interfaz docente que se encuetra en la carpeta template y la busqueda de sólo docentes de paralelo z
    """
    personasReceived = personas.find({"Rol": "Docente", "Paralelo": "Z"})
    return render_template('interfacedocente.html', personas = personasReceived)


#decorador de editar estudiante
@app.route('/editestudiantes')
def editestudiantes():
    """
     función editar estudiantes
    
    Parameters
    ------------
    variable personasReceived donde hacemos una consulta a nuestra base de datos 
    sólo los de rol estudiantes y paralelo z
     Return
     -----------
     devuelve la subpage interfaz docente que se encuetra en la carpeta template y la busqueda de sólo estudiantes de paralelo z
    """
    estudiantesReceived = estudiantes.find({"Rol": "Estudiante", "Paralelo": "Z"})

    return render_template('editestudiantes.html', estudiantes = estudiantesReceived)


#decorador de ensatis
@app.route('/ensatis')
def ensatis():
    """
     función  ensatis
    
    Parameters
    ------------
    variable personasReceived donde hacemos una consulta a nuestra base de datos 
    sólo los de rol docente y paralelo A
    ------------
    variable estudiantesReceived donde hacemos una consulta a nuestra base de datos 
    sólo los de rol estudiante y paralelo A
 
    variable paraleloReceived donde hacemos una consulta a nuestra base de datos 
    sólo paralelo A


     Return
     -----------
     devuelve la subpage ensatis que se encuetra en la carpeta template y la busqueda de sólo docentes de paralelo a
     estudiantes sólo paralelo a y paralelo a
    """
    personasReceived = personas.find({"Rol": "Docente", "Paralelo": "A"})
    estudiantesReceived = personas.find({"Rol": "Estudiante", "Paralelo": "A"})
    paraleloReceived =personas.find({"Paralelo": "A"})
    return render_template('ensatis.html',  paralelo = paraleloReceived, estudiantes =estudiantesReceived, personas = personasReceived) 


#Controlador de la interfaz principal del administrador
@app.route('/interfaceadmin')
def interfaceadmin():
    """
     función  interfaz administrador
    
    Parameters
    ------------
    variable administadorReceived donde hacemos una consulta a nuestra base de datos 

     Return
     -----------
     devuelve la subpage interfaz administrador que se encuetra en la carpeta template y la busqueda de administrador
    """
    #administador = db['administador']
    administadorReceived = administador.find()
    return render_template('interfaceadmin.html', administador = administadorReceived)

#Controlador de la interfaz principal del administrador registrando estudiantes
@app.route('/interfaceadminre')
def interfaceadminre():
    """
     función  interfaz administrador estudiantes
    
    Parameters
    ------------
    variable administadorReceived donde hacemos una consulta a nuestra base de datos de sólo rol estudiantess y estado activo
    variable paraleloReceived busqueda de sólo estado activo

     Return
     -----------
     devuelve la subpage interfaz administrador estudiantes y las dos busquedas
    """
    #estudiantes = db['personas']
    estudiantesReceived = personas.find({"Rol":"Estudiante", "Estado":"Activo"})
    paraleloReceived = paralelo.find({"Estado":"Activo"})
    return render_template('interfaceadminre.html', estudiantes = estudiantesReceived, paralelo = paraleloReceived)


#Controlador de la interfaz principal del administrador registrando docentes
@app.route('/interfaceadminrd')
def interfaceadminrd():
    """
     función  interfaz administrador docentes
    
    Parameters
    ------------
    variable administadorReceived donde hacemos una consulta a nuestra base de datos de sólo rol docente y estado activo
    variable paraleloReceived busqueda de sólo estado activo

     Return
     -----------
     devuelve la subpage interfaz administradordocente que se encuetra en la carpeta template y la busqueda de administrador
    """
    #personas = db['personas'] 
    personasReceived = personas.find({"Rol":"Docente","Estado":"Activo"})
    paraleloReceived = paralelo.find({"Estado":"Activo"})
    return render_template('interfaceadminrd.html', personas = personasReceived, paralelo = paraleloReceived)


#decorador de registrar docente
@app.route('/registerdocentes')
def registerdocentes():
    """
     función  interfaz registrar docentes
    
    Parameters
    ------------
    variable administadorReceived donde hacemos una consulta a nuestra base de datos de sólo rol docente 
    variable  aniolectivoReceived busqueda de los años lectivos

     Return
     -----------
     devuelve la subpage interfaz registrar docente que se encuetra en la carpeta template y la busqueda de rol docente y año lectivo
    """
    #personas = db['personas']
    personasReceived = personas.find({"Rol":"Docente"})
    aniolectivoReceived = aniolectivo.find()
    return render_template('registerdocentes.html', personas = personasReceived, aniolectivo = aniolectivoReceived)

#decorador de registrar estudiante
@app.route('/registerestudiantes')
def registerestudiantes():
    """
     función  interfaz registrar estudiante
    
    Parameters
    ------------
    variable administadorReceived donde hacemos una consulta a nuestra base de datos de sólo rol estudainte 
    variable  paraleloReceived busqueda de los paralelos

     Return
     -----------
     devuelve la subpage interfaz registrar docente que se encuetra en la carpeta template y la busqueda de rol estdiante  y paralelo
    """
    #estudiantes = db['personas']
    estudiantesReceived = personas.find({"Rol":"Estudiante"})
    paraleloReceived = personas.distinct("Paralelo")
    return render_template('registerestudiantes.html', estudiantes = estudiantesReceived, paralelo = paraleloReceived)

#Controlador de la interfaz principal del administrador registrando paralelos
@app.route('/interfaceadminrp')
def interfaceadminrp():
    """
     función  interfaz administradorp
    
    Parameters
    ------------
    variable paraleloReceived busqueda de los paralelos

     Return
     -----------
     devuelve la subpage interfaz administradorp que se encuetra en la carpeta template y la busqueda de rol paralelo
    """
    #paralelo = db['paralelo']
    paraleloReceived = paralelo.find()
    return render_template('interfaceadminrp.html', paralelo = paraleloReceived)


#Controlador de la interfaz principal del administrador registrando año lectivo
@app.route('/interfaceadminra')
def interfaceadminra():
    """
     función  interfaz administardorra
    
    Parameters
    ------------
    variable administadorReceived donde hacemos una consulta a nuestra base de datos

     Return
     -----------
     devuelve la subpage interfaz administradorra que se encuetra en la carpeta template y la busqueda 
    """
    #administrador = db['administrador']
    administradorReceived = administrador.find()
    return render_template('interfaceadminra.html', administrador = administradorReceived)

#--------------------------------------------------------------------------------------
#DOCENTE MODIFICA LOS DATOS DEL USUARIO PERO NO ELIMINA--------------------------------
#Method Put
@app.route('/editree/<string:eree>', methods=['POST'])
def editree(eree):
    """
     función  editree editar estudiante
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables y usamos un update para modificar al estudiante
    
    $set para setear la infromacion y guardar la actual
    response mensaje que el estudiante ha sido actualizado
     Return
     -----------
     devuelve la subpage de editar estudiante que se encuetra en la carpeta template 
    """
    #estudiantes = db['estudiantes']
    idestudiante = request.form['idestudiante']
    cedula = request.form['cedula']
    name = request.form['name']
    lastname = request.form['lastname']
    rol = request.form['rol']
    alectivo = request.form['alectivo']
    paralelo = request.form['paralelo']
    estado = request.form['estado']
    edad = request.form['edad']
    nota = request.form['nota']
    entrena = request.form['entrena']

    if name and rol and edad and nota and idestudiante and cedula and lastname and alectivo and paralelo and estado:
        estudiantes.update_one({'Nombre' : eree}, 
            {'$set' : {
            '_id': idestudiante,
            'Cedula': cedula,
            'Nombre' : name,
            'Apellido' : lastname,
            'Rol' : rol,
            'Añolectivo' : alectivo,
            'Paralelo': paralelo,
            'Estado': estado,
            'Edad' : edad,
            'Nota' : nota,
            'Entrenamiento' : entrena
                }})
        response = jsonify({'message' : 'Estudiante ' + eree + ' actualizado correctamente'})
        return redirect(url_for('editestudiantes'))
    else:
        return notFound1()
#--------------------------------------------------------------------------------------
#ADMIN REGISTRA UN DOCENTE-------------------------------------------------------------
@app.route('/docente', methods=['POST'])
def addDocente():
    """
     función  addDocente agregar  docente con metodo post sólo admin
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables y usamos un update para añadir docente

     Return
     -----------
     devuelve la subpage de añadir docente que se encuetra en la carpeta template 
    """
    #personas = db['personas']
    iddocente = request.form['iddocente']
    cedula = request.form['cedula']
    name = request.form['name']
    lastname = request.form['lastname']
    rol = request.form['rol']
    alectivo = request.form['alectivo']
    paralelo = request.form['paralelo']
    estado = request.form['estado']
    mail = request.form['mail']
    pwd = request.form['pwd']

    if name and mail and rol and estado and pwd and iddocente and cedula and lastname  and alectivo and paralelo:
        dbdocente = Docente(iddocente, cedula, name, lastname, rol, alectivo, paralelo,estado, mail, pwd)
        personas.insert_one(dbdocente.toDBCollection())
        response = jsonify({
            '_id': iddocente,
            'Cedula': cedula,
            'Nombre' : name,
            'Apellido' : lastname,
            'Rol' : rol,
            'Añolectivo' : alectivo,
            'Paralelo': paralelo,
            'Estado': estado,
            'CorreoElectronico' : mail,
            'Contraseña' : pwd
        })
        return redirect(url_for('interfaceadminrd'))
    else:
        return notFound()

#ADMIN ELIMINA UN DOCNETE
@app.route('/deleterd/<string:erd>')
def deleterd(erd):
    """
     función  deleted eliminar  docente sólo admin
    
    Parameters
    ------------
    vllamamos a la coleccion personas  eliminamos docente

     Return
     -----------
     devuelve la subpage de añadir docente que se encuetra en la carpeta template 
    """
    #personas = db['personas']
    personas.delete_one({'Nombre' : erd})
    return redirect(url_for('registerdocentes'))

#ADMIN EDITA LOS DATOS DE UN DOCENTE
@app.route('/editrd/<string:erd>', methods=['POST'])
def editrd(erd):
    """
     función  editred editar docente
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables y usamos un update para modificar docente
    
    $set para setear la infromacion y guardar la actual
    response mensaje que el estudiante ha sido actualizado
     Return
     -----------
     devuelve la subpage de añadir docente que se encuetra en la carpeta template 
    """
    #personas = db['personas']
    iddocente = request.form['iddocente']
    cedula = request.form['cedula']
    name = request.form['name']
    lastname = request.form['lastname']
    rol = request.form['rol']
    alectivo = request.form['alectivo']
    paralelo = request.form['paralelo']
    estado = request.form['estado']
    mail = request.form['mail']
    pwd = request.form['pwd']

    if name and rol and mail and pwd and iddocente and cedula and lastname and alectivo and paralelo and estado:
        personas.update_one({'Nombre' : erd}, 
            {'$set' : {
            '_id': iddocente,
            'Cedula': cedula,
            'Nombre' : name,
            'Apellido' : lastname,
            'Rol' : rol,
            'Añolectivo' : alectivo,
            'Paralelo': paralelo,
            'Estado': estado,
            'CorreoElectronico' : mail,
            'Contraseña' : pwd
                }})
        response = jsonify({'message' : 'Docente ' + erd + ' actualizado correctamente'})
        return redirect(url_for('registerdocentes'))
    else:
        return notFound()
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#ADMIN AGREGA UN ESTUDIANTE
@app.route('/estudiantes', methods=['POST'])
def addEstudiante():
    """
     función addEstudainte con metodo POST
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables para añadir estudiante

     Return
     -----------
     devuelve la subpage de añadir estudiante que se encuetra en la carpeta template 
    """
    #estudiantes = db['personas']
    idestudiante = request.form['idestudiante']
    cedula = request.form['cedula']
    name = request.form['name']
    lastname = request.form['lastname']
    edad = request.form['edad']
    rol = request.form['rol']
    alectivo = request.form['alectivo']
    paralelo = request.form['paralelo']
    estado = request.form['estado']


    if name and rol and idestudiante and cedula and lastname and edad and alectivo and paralelo and estado:
        dbestudiante = Estudiante(idestudiante, cedula, name, lastname, rol, alectivo,paralelo,estado, edad)
        estudiantes.insert_one(dbestudiante.toDBCollection())
        response = jsonify({
            '_id': idestudiante,
            'Cedula': cedula,
            'Nombre' : name,
            'Apellido' : lastname,
            'Edad' : edad,
            'Rol' : rol,
            'Año lectivo' : alectivo,
            'Paralelo': paralelo,
            'Estado': estado,
            'Nota': "0",
            'Entrenamiento': "0"

        })
        return redirect(url_for('interfaceadminre'))
    else:
        return notFound1()

#ADMIN ELIMINA ESTUDIANTE
@app.route('/deletere/<string:ere>')
def deletere(ere):
    """
     función  deletee eliminar estudiante sólo admin
    
    Parameters
    ------------
    vllamamos a la coleccion personas  eliminamos docente

     Return
     -----------
     devuelve la subpage de añadir estudiante que se encuetra en la carpeta template 
    """
    #estudiantes = db['personas']
    estudiantes.delete_one({'Nombre' : ere})
    return redirect(url_for('registerestudiantes'))

#ADMIN MODIFICA LOS DAOTS DE UN ESTUDIANTE
@app.route('/editre/<string:ere>', methods=['POST'])
def editre(ere):
    """
     función  editred editar estudainte
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables y usamos un update para modificar estudiante
    
    $set para setear la infromacion y guardar la actual
    response mensaje que el estudiante ha sido actualizado
     Return
     -----------
     devuelve la subpage de añadir  estudiante que se encuetra en la carpeta template 
    """
    #estudiantes = db['personas']
    idestudiante = request.form['idestudiante']
    cedula = request.form['cedula']
    name = request.form['name']
    lastname = request.form['lastname']
    rol = request.form['rol']
    alectivo = request.form['alectivo']
    paralelo = request.form['paralelo']
    estado = request.form['estado']
    edad = request.form['edad']
    nota = request.form['nota']
    entrena = request.form['entrena']

    if name and rol and edad and nota and idestudiante and cedula and lastname and alectivo and paralelo and estado:
        estudiantes.update_one({'Nombre' : ere}, 
            {'$set' : {
            '_id': idestudiante,
            'Cedula': cedula,
            'Nombre' : name,
            'Apellido' : lastname,
            'Rol' : rol,
            'Añolectivo' : alectivo,
            'Paralelo': paralelo,
            'Estado': estado,
            'Edad' : edad,
            'Nota' : nota,
            'Entrenamiento' : entrena
                }})
        response = jsonify({'message' : 'Estudiante ' + ere + ' actualizado correctamente'})
        return redirect(url_for('registerestudiantes'))
    else:
        return notFound()
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#MADMIN AGREGA UN NUEVO CURSO----------------------------------------------------------
@app.route('/paralelo', methods=['POST'])
def addParalelo():
    """
     función addParalelo con metodo POST
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables para añadir paralelo

     Return
     -----------
     devuelve la subpage de añadir paralelo que se encuetra en la carpeta template 
    """
    #paralelo = db['paralelo']
    idparalelo = request.form['idparalelo']
    descripcion = request.form['descripcion']
    estado = request.form['estado']

    if idparalelo and descripcion  and estado:
        dbparalelo = Paralelo(idparalelo, descripcion, estado)
        paralelo.insert_one(dbparalelo.toDBCollection())
        response = jsonify({
            '_id': idparalelo,
            'Descripcion': descripcion,
            'Estado' : estado,
        })
        return redirect(url_for('interfaceadminrp'))
    else:
        return notFound()

#ADMIN EDITA UN CURSO
@app.route('/editrp/<string:erp>', methods=['POST'])
def editrp(erp):
    """
     función  editrep editar pralelo
    
    Parameters
    ------------
    variable de los campos correspondientes del formulario y llAamos con name a los campos del formulario
    if anidamos las variables y usamos un update para modificar paralelo
    
    $set para setear la infromacion y guardar la actual
    response mensaje que el estudiante ha sido actualizado
     Return
     -----------
     devuelve la subpage de añadir  paralelo que se encuetra en la carpeta template 
    """
    #paralelo = db['paralelo']
    idparalelo = request.form['idparalelo']
    descripcion = request.form['descripcion']
    estado = request.form['estado']

    if idparalelo and descripcion and estado:
        paralelo.update_one({'Descripcion' : erp}, 
            {'$set' : {
            '_id': idparalelo,
            'Descripcion': descripcion,
            'Estado' : estado
                }})
        response = jsonify({'message' : 'Paralelo ' + erp + ' actualizado correctamente'})
        return redirect(url_for('interfaceadminrp'))
    else:
        return notFound()

#ADMIN ELIMINA UN CURSO
@app.route('/deleterp/<string:erp>')
def deleterp(erp):
    """
     función  deletep eliminar paralelo sólo admin
    
    Parameters
    ------------
    vllamamos a la coleccion personas  eliminamos paraleloS

     Return
     -----------
     devuelve la subpage de añadir paralelo que se encuetra en la carpeta template 
    """
    #paralelo = db['paralelo']
    paralelo.delete_one({'Descripcion' : erp})
    return redirect(url_for('interfaceadminrp'))

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#Errores
@app.errorhandler(404)
def notFound(error=None):
    """
     función notFound para errores
    
    Parameters
    ------------
   mensaje de no encontrado
   estado 
   devolcemos el mensaje
   devolvemos el codigo 404 not found

     Return
     -----------
     devuelve response
    """
    message = {
    'message':'No encontrado' + request.url,
    'status':'404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#ERROR DE ID DUPLICADO 
@app.errorhandler(pymongo.errors.DuplicateKeyError)
def notFound1(error=None):
    """
     función  ntfound1 
    
    Parameters
    ------------
    
    mensaje de duplicado
    devolvemos estado
     Return
     -----------
     devuelve responseD
    """
    message = {
    'message':'ID DUPLICADA' + request.url,
    'status':'304 Not Found'
    }
    responseD = jsonify(message)
    responseD.status_code = 304
    return responseD


#Corre la app
if __name__ == '__main__':
    app.run(debug=True)