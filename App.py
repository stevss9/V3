from flask import Flask, render_template, request, Response, jsonify, redirect, url_for, flash, session
import pymongo
import os

import database as dbase 
from dbestudiante import Estudiante
from dbdocente import Docente 
from dbparalelo import Paralelo
from dbadministrador import Administrador



db = dbase.dbConnection()

app = Flask(__name__) 
app._static_folder = os.path.abspath("static/")

#Controlador de la ruta inicial
@app.route('/')
def principal():
    return render_template('principalmain.html')
#Controlador del login
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginn')
def loginn():
    return render_template('loginn.html')

@app.route('/traingame')
def traingame():
    return render_template('traingame.html')

@app.route('/menugame')
def menugame():
    return render_template('menugame.html')

@app.route('/evaluationgame')
def evaluationgame():
    return render_template('evaluationgame.html')

@app.route('/interfacedocente')
def interfacedocente():
    return render_template('interfacedocente.html')

@app.route('/editestudiantes')
def editestudiantes():
    estudiantes = db['estudiantes']
    estudiantesReceived = estudiantes.find()

    return render_template('editestudiantes.html', estudiantes = estudiantesReceived)

@app.route('/ensatis')
def ensatis():
    return render_template('ensatis.html')


#Controlador de la interfaz principal del administrador
@app.route('/interfaceadmin')
def interfaceadmin():
    administador = db['administador']
    administadorReceived = administador.find()
    return render_template('interfaceadmin.html', administador = administadorReceived)

#Controlador de la interfaz principal del administrador registrando estudiantes
@app.route('/interfaceadminre')
def interfaceadminre():
    estudiantes = db['estudiantes']
    estudiantesReceived = estudiantes.find()

    return render_template('interfaceadminre.html', estudiantes = estudiantesReceived)


#Controlador de la interfaz principal del administrador registrando docentes
@app.route('/interfaceadminrd')
def interfaceadminrd():
    personas = db['personas']
    personasReceived = personas.find()
    return render_template('interfaceadminrd.html', personas = personasReceived)

@app.route('/registerdocentes')
def registerdocentes():
    personas = db['personas']
    personasReceived = personas.find()
    return render_template('registerdocentes.html', personas = personasReceived)

@app.route('/registerestudiantes')
def registerestudiantes():
    estudiantes = db['estudiantes']
    estudiantesReceived = estudiantes.find()
    return render_template('registerestudiantes.html', estudiantes = estudiantesReceived)

#Controlador de la interfaz principal del administrador registrando paralelos
@app.route('/interfaceadminrp')
def interfaceadminrp():
    paralelo = db['paralelo']
    paraleloReceived = paralelo.find()
    return render_template('interfaceadminrp.html', paralelo = paraleloReceived)


#Controlador de la interfaz principal del administrador registrando año lectivo
@app.route('/interfaceadminra')
def interfaceadminra():
    administrador = db['administrador']
    administradorReceived = administrador.find()
    return render_template('interfaceadminra.html', administrador = administradorReceived)

#--------------------------------------------------------------------------------------
#DOCENTE MODIFICA LOS DATOS DEL USUARIO PERO NO ELIMINA--------------------------------
#Method Put
@app.route('/editree/<string:eree>', methods=['POST'])
def editree(eree):
    estudiantes = db['estudiantes']
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
        return notFound()
#--------------------------------------------------------------------------------------
#ADMIN REGISTRA UN DOCENTE-------------------------------------------------------------
@app.route('/docente', methods=['POST'])
def addDocente():
    personas = db['personas']
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
    personas = db['personas']
    personas.delete_one({'Nombre' : erd})
    return redirect(url_for('registerdocentes'))

#ADMIN EDITA LOS DATOS DE UN DOCENTE
@app.route('/editrd/<string:erd>', methods=['POST'])
def editrd(erd):
    personas = db['personas']
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
    estudiantes = db['estudiantes']
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
    estudiantes = db['estudiantes']
    estudiantes.delete_one({'Nombre' : ere})
    return redirect(url_for('registerestudiantes'))

#ADMIN MODIFICA LOS DAOTS DE UN ESTUDIANTE
@app.route('/editre/<string:ere>', methods=['POST'])
def editre(ere):
    estudiantes = db['estudiantes']
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
    paralelo = db['paralelo']
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
    paralelo = db['paralelo']
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
    paralelo = db['paralelo']
    paralelo.delete_one({'Descripcion' : erp})
    return redirect(url_for('interfaceadminrp'))

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#Errores
@app.errorhandler(404)
def notFound(error=None):
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
    message = {
    'message':'ID DUPLICADA' + request.url,
    'status':'304 Not Found'
    }
    responseD = jsonify(message)
    responseD.status_code = 304
    return responseD


if __name__ == '__main__':
    app.run(debug=True)