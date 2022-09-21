from flask import Flask, render_template, url_for
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/registro')
def registro():
	return render_template('registro.html')

@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/usuarios')
def usuarios():
	return render_template('usuarios.html')

@app.route('/materias')
def materias():
	return render_template('materias.html')

@app.route('/cursos')
def cursos():
	return render_template('cursos.html')

@app.route('/matriculas')
def matriculas():
	return render_template('matriculas.html')

@app.route('/calificaciones')
def calificaciones():
	return render_template('calificaciones.html')

@app.route('/actividades')
def actividades():
	return render_template('actividades.html')

@app.route('/personal')
def personal():
	return render_template('personal.html')

@app.route('/notas')
def notas():
	return render_template('notas.html')

if __name__=='__main__':
	app.run(debug=True)