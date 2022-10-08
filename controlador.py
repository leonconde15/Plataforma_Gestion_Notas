import sqlite3

import envioemail
from datetime import datetime
from flask import flash
DB_NAME='gestion.s3db'

def conectar_bd():
    conexion=sqlite3.connect(DB_NAME)
    return conexion
#Ingresar Usuarios    
def insertar_usuarios(nom,ape,email,usuario,rol,contra,nac):
    cod_ver=str(datetime.now())
    cod_ver=cod_ver.replace("-","")
    cod_ver=cod_ver.replace(" ","")
    cod_ver=cod_ver.replace(":","")
    cod_ver=cod_ver.replace(".","")
    
    try:
        bd=conectar_bd()
        cursor=bd.cursor()
        sql="INSERT INTO usuarios(nombre,apellido,email,usuario,rol,contrasena,nacimiento,cod_verificacion,verificado) VALUES(?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,[nom,ape,email,usuario,rol,contra,nac,cod_ver,0])
        bd.commit()
        envioemail.enviar_email(email,cod_ver)
        return True
    except:
        return False

# Ingresar Materias
def insertar_materias(nombre):
    try:
        bd=conectar_bd()
        cursor=bd.cursor()
        sql="INSERT INTO materia(nombre_materia) VALUES(?)"
        cursor.execute(sql,[nombre])
        bd.commit()
        return True
    except:
        return False

# Ingresar Matricula
def insertar_matricula(id_materia,id_docente,id_estudiante):
    try:
        bd=conectar_bd()
        cursor=bd.cursor()
        sql="INSERT INTO matricula(id_materia,id_docente,id_estudiante) VALUES(?,?,?)"
        cursor.execute(sql,[id_materia,id_docente,id_estudiante])
        bd.commit()
        return True
    except:
        return False

def validar_usuarios(username):
    try:
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM usuarios WHERE usuario=?"
        cursor.execute(sql,[username])
        resultado=cursor.fetchone()
        
        usuario=[
            {
            'id_usuario':resultado[0],
            'nombre':resultado[1],
            'apellido':resultado[2],
            'email':resultado[3],
            'usuario':resultado[4],
            'rol':resultado[5],
            'contrasena':resultado[6],
            'nacimiento':resultado[7],
            'cod_verificacion':resultado[8], 
            'verificado':resultado[9] 
            
            }
            ]
        return usuario
           
    except:
        return False

def activar_usuario(username,codver):
    try:
        db=conectar_bd()
        cursor=db.cursor()
        sql='UPDATE usuarios SET verificado=1 WHERE usuario=? AND cod_verificacion=?'
        cursor.execute(sql,[username,codver])
        db.commit()
        return True      
    except:
        return False
# Traer Materias de la base de datos
def lista_materias():
    try:
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM materia"
        cursor.execute(sql)
        resultado=cursor.fetchall()
        materia=[]
        for mater in resultado:
            regist={
                    'id_materia':mater[0],
                    'nombre_materia':mater[1]                                
                 }
            materia.append(regist)    
        return materia
           
    except:
        return False
# Traer a los usuarios
def listar_usuarios(username):
    try:
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM usuarios WHERE usuario=?"
        cursor.execute(sql,[username])
        resultado=cursor.fetchall()
        usuarios=[]
        for u in resultado:
            registro = {
                'id':u[0],
                'nombre':u[1],
                'apellido':u[2],
                'email':u[3],
                'usuario':u[4],
                'nacimiento':u[7]
                }
            usuarios.append(registro)    

                
        return usuarios   
    except:
        return False

# Traer los roles activos 
def listar_roles(username):
    try:
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM roles,usuarios WHERE usuario=? AND rol=id_rol"
        cursor.execute(sql,[username])
        resultado=cursor.fetchall()
        roles=[]
        for u in resultado:
            registro = {
                'id_rol':u[0],
                'nombre_rol':u[1]                
                }
            roles.append(registro)    

        print(roles)        
        return roles
           
    except:
        return False
# Traer Docentes de la base de datos
def lista_docentes():
    try:
        roles=2
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM usuarios WHERE rol=?"
        cursor.execute(sql,[roles])
        resultado=cursor.fetchall()
        docente=[]
        for doc in resultado:
            regist={
                    'id_usuario':doc[0],
                    'nombre':doc[1],
                    'apellido':doc[2]                                
                 }
            docente.append(regist)    
        return docente
    except:
        return False

# Traer Estudiantes de la base de datos
def lista_estudiantes():
    try:
        roles=3
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM usuarios WHERE rol=?"
        cursor.execute(sql,[roles])
        resultado=cursor.fetchall()
        estudiante=[]
        for est in resultado:
            regist={
                    'id_usuario':est[0],
                    'nombre':est[1],
                    'apellido':est[2]                                
                 }
            estudiante.append(regist)    
        return estudiante
    except:
        return False
# Traer a todos los usuarios
def todos_usuarios():
    usuarios=[]
    try:
        db=conectar_bd()
        cursor=db.cursor()
        sql="SELECT * FROM usuarios"
        cursor.execute(sql)
        resultado=cursor.fetchall()
        
        for u in resultado:
            registro = {
                'id':u[0],
                'nombre':u[1],
                'apellido':u[2],
                'email':u[3],
                'usuario':u[4]
                }
            usuarios.append(registro)                
        return usuarios   
    except:
        registro={
            'resultado':'No Existen Mensajes'
             }
        usuarios.append(registro)
    return usuarios
