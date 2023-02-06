#from my_app import app
from flask import Blueprint

hello = Blueprint('hello',__name__)

@hello.route('/')
@hello.route('/hola')
def metodo_hola():
    return "Hola mundo"