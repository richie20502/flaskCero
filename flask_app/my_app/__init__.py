from flask import Flask
from my_app.hello1.views import hello

app = Flask(__name__)
app.register_blueprint(hello)

#importacion de las vistas
#import my_app.hello1.views