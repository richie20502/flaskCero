from flask import Flask
from my_app.product.views import product

app = Flask(__name__)
app.register_blueprint(product)

#importacion de las vistas
#import my_app.hello1.views
@app.template_filter('mydouble')
def mydouble_filter(n):
    return n*2