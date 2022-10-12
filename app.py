from datetime import date, datetime
from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
import controlador
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)

app.secret_key='clave secreta'+str(datetime.now)


@app.route('/activar', methods=['POST'])
def activa_cuenta():
	datos=request.form
	username=datos['usuario']
	codver=datos['codigo_verificacion']
	resultado=controlador.activar_usuario(username,codver)
	if resultado:
		flash('Cuenta Activada Satisfactoriamente')

	else:
		flash('Error en Activacion')
	return redirect(url_for('verificacion'))

@app.route('/validacionlogin', methods=['POST'])
def val_user():	
    datos=request.form
    username=datos['usuario']
    passwd=datos['contrasena']
	
    if username=='' or passwd=='':
        flash('Datos Incompletos')
    else:
        resultado=controlador.validar_usuarios(username)
        if resultado==False:
            flash('Error al Ingresar')
            return redirect(url_for('login'))
        else:
            print('Resultado: '+ str(resultado[0]['verificado']))
            if(resultado[0]['verificado']==1):
            
                if check_password_hash(resultado[0]['contrasena'],passwd):
                    session['usuario']=username
                    session['nombre']=resultado[0]['nombre'] +" "+resultado[0]['apellido']
                    
                    listadouser=controlador.listar_usuarios(username)
                    listadorol=controlador.listar_roles(username)
                    listadoidusuario=controlador.listar_id_usuario(username)
                    session['nombre_rol']=listadorol[0]['nombre_rol']
                    session['id_usuario']=listadoidusuario[0]['id_usuario']
                    return render_template('menu.html',datauser=listadouser)					
                    
                else:
                    flash('Contraseña Invalida')
                    return redirect(url_for('login'))

            else:
                return redirect(url_for('verificacion'))


#Recuperar información desde los formularios
#formulario de usuarios
@app.route('/agregarusuario', methods=['POST'])
def agregar_usuario():
	datos=request.form
	nombre=datos['nombre']
	apellido=datos['apellido']
	email=datos['email']
	usuario=datos['usuario']
	rol=datos['rol']
	contrasena=datos['contrasena']
	contrasena2=datos['contrasena2']
	fnacimiento=datos['fnacimiento']
	contrasenaencript=generate_password_hash(contrasena)

	if nombre=='' or apellido=='' or email=='' or usuario=='' or rol=='' or contrasena=='' or contrasena2=='' or fnacimiento=='':
		flash('Datos incompletos')
	elif len(contrasena)<6:
		flash('La contraseña debe ser igual o mayor a 6 caracteres')
	elif contrasena!=contrasena2:
		flash('Las contraseñas no son iguales')
	else:
		resultado=controlador.insertar_usuarios(nombre,apellido,email,usuario,rol,contrasenaencript,fnacimiento)
		if resultado:
			flash('Información Guardada')
		else:
			flash('Error de Registro')
	return redirect(url_for('usuarios'))
    

@app.route('/agregarmateria', methods=['POST'])
def agregar_materias():
	datos=request.form
	nombremateria=datos['nombremateria']
	resultado2=controlador.insertar_materias(nombremateria)
	if resultado2:
		flash('Información Guardada')
	else:
		flash('Error de Registro')
	return redirect(url_for('materias'))
#agregar matricula
@app.route('/agregarmatricula', methods=['POST'])
def agregar_matricula():
	datos=request.form
	id_materia=datos['materia']
	id_docente=datos['docente']
	id_estudiante=datos['estudiante']
	resultado2=controlador.insertar_matricula(id_materia,id_docente,id_estudiante)
	if resultado2:
		flash('Información Guardada')
	else:
		flash('Error de Registro')
	return redirect(url_for('matriculas'))

#agregar actividad
@app.route('/agregaractividad', methods=['POST'])
def agregar_actividad():
	datos=request.form
	id_materia=datos['materia']
	id_docente=datos['docente']
	nombre_actividad=datos['actividad']
	resultado2=controlador.insertar_actividad(id_materia,id_docente,nombre_actividad)
	if resultado2:
		flash('Información Guardada')
	else:
		flash('Error de Registro')
	return redirect(url_for('actividades'))

#agregar calificacion
@app.route('/agregarcalificacion', methods=['POST'])
def agregar_calificacion():
	datos=request.form
	id_materia=datos['materia']
	id_estudiante=datos['estudiante']
	id_docente=datos['docente']
	id_actividad=datos['actividad']
	nota=datos['nota']
	retroalimentacion=datos['retro']
	resultado2=controlador.insertar_calificacion(id_materia,id_estudiante,id_docente,id_actividad,nota,retroalimentacion)
	if resultado2:
		flash('Información Guardada')
	else:
		flash('Error de Registro')
	return redirect(url_for('calificaciones'))



# LISTAR USUARIOS
@app.route('/listadousuarios', methods=['GET','POST'])
def lista_usuarios():
	listado=controlador.todos_usuarios()
	return jsonify(listado)

# LISTAR MATERIAS
@app.route('/listadomaterias', methods=['GET','POST'])
def lista_materias():
	listado=controlador.lista_materias()
	return jsonify(listado)

# LISTAR PERSONAL
@app.route('/listadopersonal', methods=['POST'])
def lista_personal():
	datos=request.get_json()
	username=datos['usuario']
	listado=controlador.listar_usuarios(username)
	return jsonify(listado)

# LISTAR ACTIVIDAD INDIVIDUAL
@app.route('/listaactividad', methods=['POST'])
def lista_actividad():
	datos=request.get_json()
	username=datos['usuario']
	listado=controlador.lista_actividadindv(username)
	return jsonify(listado)

# LISTAR NOTAS
@app.route('/listanotas', methods=['POST'])
def lista_notas():
	datos=request.get_json()
	username=datos['usuario']
	listado=controlador.listar_notas(username)
	return jsonify(listado)

# LISTAR PROMEDIO GENERAL
@app.route('/listapromedio', methods=['POST'])
def lista_promedio():
	datos=request.get_json()
	username=datos['usuario']
	listado=controlador.listar_promedio(username)
	return jsonify(listado)
	

#LISTAR ESTUDIANTES PARA CALIFICAR
@app.route('/estcal', methods=['POST'])
def lista_estcal():
	
	username2=session['id_usuario']
	listado=controlador.listar_estudiantescalif(username2)
	return jsonify(listado)

# LISTAR USUARIOS
@app.route('/listadomatriculados', methods=['GET','POST'])
def lista_matriculados():
	listado=controlador.lista_matriculados()
	return jsonify(listado)


#RUTAS DE NAVEGACION ##########
@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login')
def login():
	session.clear()
	return render_template('login.html')

@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/usuarios')
def usuarios():
	return render_template('usuarios.html')

@app.route('/materias')
def materias():
	return render_template('materias.html')

@app.route('/matriculas')
def matriculas():
	listadomaterias=controlador.lista_materias()
	listadodocente=controlador.lista_docentes()
	listadoestudiante=controlador.lista_estudiantes()
	return render_template('matriculas.html',datosmateria=listadomaterias,datosdocente=listadodocente,datosestudiante=listadoestudiante)

@app.route('/calificaciones')
def calificaciones():
	username=session['usuario']
	username2=session['id_usuario']
	listadocalificaciones=controlador.lista_materiasindv(username)
	listadoactividad=controlador.lista_actividadindv(username)
	listadoestudiante=controlador.lista_estudianteindv(username2)
	return render_template('calificaciones.html',datosmatind=listadocalificaciones,datosactvind=listadoactividad,datosestudiante=listadoestudiante)

@app.route('/actividades')
def actividades():
	username=session['usuario']
	listadocalificaciones=controlador.lista_materiasindv(username)
	return render_template('actividades.html',datosmatind=listadocalificaciones)
	

@app.route('/personal')
def personal():
	return render_template('personal.html')

@app.route('/notas')
def notas():
	return render_template('notas.html')

@app.route('/verificacion')
def verificacion():
	return render_template('verificacion.html')


# AQUI SE PROTEGEN TODAS LAS RUTAS SI NO ESTA LOGUEADO
@app.before_request
def proteger_enlaces():
	enlace=request.path

	if not 'usuario' in session and (enlace=='/menu' or enlace=='/usuarios' or enlace=='/materias' or enlace=='/matriculas' or enlace=='/calificaciones' or enlace=='/actividades' or enlace=='/personal' or enlace=='/notas'):
		flash('Por favor tiene que loguearse en el sistema')
		return redirect('/login')


if __name__=='__main__':
	app.run(debug=True)