from my_app import app

@app.route('/hola')
def metodo_hola():
    return "Hola mundo"