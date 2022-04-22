from flask import render_template
from flask import render_template
from flask import Flask, render_template, request
from . import portafolio

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('token.json')
firebase_admin.initialize_app(cred)

# Para conectarse a firestore

from firebase_admin import firestore

db = firestore.client()

app = Flask(__name__)

@portafolio.route('/')
def home():
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
    return render_template('portafolio/home.html', **context)