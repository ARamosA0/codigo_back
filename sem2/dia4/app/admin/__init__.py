from flask import Blueprint
# Bluprint => Sirve para crear un modulo de flask, extructurar mi codigo, 
#toda la  nadministracion estar a en admin
# Se crean  Blueprint deacuerdo a la funcionalidad  que se le quiera dar
# Se puede crear tambien por tipo de aplicacion 
# Modulos de la empresa 
# En cada carpeta se tendra una seccion 
admin = Blueprint('admin', __name__, url_prefix='/admin')

from . import views