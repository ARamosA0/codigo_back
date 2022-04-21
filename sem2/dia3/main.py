from multiprocessing import context
from flask import Flask, render_template, request
import requests


URL = 'https://api.github.com/users/ARamosA0'


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

# Para conectarse a firestore

from firebase_admin import firestore

db = firestore.client()


app = Flask(__name__)

@app.route('/')
def home():
    #return '<center><h1>Bienvenido a mi sitio Web</h1></center>'
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    colEnlaces = db.collection('enlaces')
    docEnlaces = colEnlaces.get()
    lstEnlaces = []
    for doc in docEnlaces:
        dicEnlaces = doc.to_dict()
        lstEnlaces.append(dicEnlaces)

    for doc in docBiografia:
        dicBiografia = doc.to_dict()
    context = {
        'biografia': dicBiografia,
        'enlaces': lstEnlaces
    }
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
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    for doc in docBiografia:
        dicBiografia = doc.to_dict()
    context = {
        'biografia': dicBiografia
    }
    return render_template('acercade.html', **context)


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
    
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    for doc in docBiografia:
        dicBiografia = doc.to_dict()

    context = {
        'proyectos':lstProyectos,
        'biografia': dicBiografia
    }
    return render_template('portafolio.html', **context)

@app.route('/contacto')
def contacto():
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    for doc in docBiografia:
        dicBiografia = doc.to_dict()
    context = {
        'biografia': dicBiografia
    }
    return render_template('contacto.html', **context)

app.run(debug=True)