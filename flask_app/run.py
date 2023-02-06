from my_app import app

#app.config.from_pyfile('config.py')
app.config.from_object('configuration.DevelopmentConfig')


#app.run(debug = True)
app.run()
#app.config['debug'] = True
#app.debug = True