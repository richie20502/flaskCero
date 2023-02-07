#from my_app import app
from flask import Blueprint
from my_app.product.model.products import PRODUCTS

product = Blueprint('product',__name__)

@product.route('/')
@product.route('/home')
def index():
    print(PRODUCTS.items())
    return "Hola mundo"