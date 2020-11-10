from flask import Flask,request,render_template
from flask_cors import CORS
import json
from Codigos import Co
Codigos=Co()
app = Flask(__name__)
CORS(app)

#modify acount
@app.route('/modiii', methods=['POST']) #mody
def prueba():
    Rp=request.json
    if Codigos.ModifiCaUser(Rp['nombre'],Rp['apellido'],Rp['username'],Rp['password'],Rp['Cpassword']):
           return "{\"data\":\"true\"}"
    else:
          return "{\"data\":\"false\"}"


#who init sesion?
@app.route('/ModiUser')
def UserAModificar():
    return Codigos.DataUser()

@app.route('/usuarioss') #lista de usuarios
def TablaUsers():
    return Codigos.VerUsers() 

#elimna msuica
@app.route('/eliminarcancion', methods=['POST']) 
def elimanaapp():
    deletee=request.json 
    if Codigos.Eliminaa(deletee['id']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"

@app.route('/mod', methods=['POST']) #musica modif
def prueba1():
    mimusica=request.json 
    if Codigos.MusicaModificar(mimusica['nombre'],mimusica['artista'],mimusica['album'],mimusica['fecha'],mimusica['ima'],mimusica['links'],mimusica['linky']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"

@app.route('/DatosCancion')
def CancionModi():
    return Codigos.ModiCancionData()

@app.route('/id', methods=['POST']) #ver si existe y guardar el id
def modificarapp():
    idd=request.json    
    if Codigos.id(idd['id']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"

@app.route('/pdf')
def pdf():
    return Codigos.Genera()

@app.route('/pdf_users')
def pdf_users():
    return Codigos.Userss()

@app.route('/') 
def index():
    return ''

@app.route('/insertar',methods=['POST']) 
def insertar(): #registro
    datos=request.json 
    if datos['password'] == datos["ConfirPassword"]:
        if Codigos.registrar(datos['nombre'], datos['apellido'], datos['username'], datos['password'], datos['ConfirPassword']):
            return "{\"datas\":\"verdadero\"}"
        else: 
            return "{\"datas\":\"false\"}"
    else: 
        return "{\"datas\":\"Diferente\"}"        

@app.route('/ingresar',methods=['POST'])    
def ingresar():
    datosi=request.json
    if datosi['username']=="admin":
        Codigos.UserActivo=0
        return "{\"datas\":\"maestro\"}"
    if Codigos.Ingresar(datosi['username'], datosi['password']):
        return "{\"datas\":\"verdadero\"}"
    else:
        return "{\"datas\":\"falso\"}"

@app.route('/recuperar',methods=['POST'])   
def recuperarc():
    lacontra=request.json
    return Codigos.Recuperar(lacontra['username'])

@app.route('/canciones', methods=['POST']) #insertar los datos en un vector
def readd():
    ar=request.json
    return Codigos.archivo(ar['a0'],ar['a1'],ar['a2'],ar['a3'],ar['a4'],ar['a5'],ar['a6'])

@app.route('/musicalista')
def usuarios():
    return Codigos.musicajson()

@app.route('/cancionesdisponibles')
def cancionesu():
    return Codigos.musicajson()    

if __name__=='__main__':  #server port=50000
    app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)