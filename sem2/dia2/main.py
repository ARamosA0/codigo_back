from multiprocessing import context
from flask import Flask, render_template, request
import requests

URL = 'https://api.github.com/users/ARamosA0'


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("tokenfirebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

@app.route('/')
def home():
    #return '<center><h1>Bienvenido a mi sitio Web</h1></center>'
    data = requests.get(URL)
    context = data.json()
    return render_template('home.html', **context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA', 'ENCANTO', 'SONIC 2']
    nombre = request.args.get('nombre','no hay nombre')
    context ={
        'peliculas':listaPeliculas,
        'nombre': nombre
    }
    return render_template('peliculas.html', **context)

######################### RUTAS DE MIS PAGINAS

@app.route('/acercade')
def about():
    return render_template('acercade.html')


@app.route('/portafolio')
def portafolio():
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()

    #print(docProyectos)

    lstProyectos = []
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)

    context = {
        'proyectos':lstProyectos
    }
    return render_template('portafolio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)