from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/template/<name>')
def template(name="Richie"):
    return render_template('view.html',vname=name)

if __name__ == '__main__':
    app.run(debug=True)