from flask import Flask
import os
##from flask_sqlalchemy import SQLAlchemy



## -------------------------------------------------------------------------------------------
## App & Config: from config.py depending on environment variable 'APP_SETTINGS'
## local development environment configured to use 'local Postgres server with DB fortnitevs'
## remote production development environment configured to use 'Postgres on Heroku'
## -------------------------------------------------------------------------------------------

def getEnvironmentVariable(varName):
	try:
		return os.environ[varName]

	except KeyError:
		mensaje = (
			f"La configuración de la aplicación necesita una variable de entorno de configuración '{varName}'.\n"
			f"Para desarrollo local:		$ export APP_SETTINGS=config.DevelopmentConfig\n"
			f"Para produccion en Heroku: 	$ heroku config:set APP_SETTINGS=config.ProductionConfig --remote heroku\n"
		)
		raise Exception(mensaje)

app = Flask(__name__)
app.config.from_object(getEnvironmentVariable('APP_SETTINGS'))
## app.config.from_object(os.environ['APP_SETTINGS'])
## app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or os.urandom(24)
print(f"Running with Config: '{os.environ['APP_SETTINGS']}'")

##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
##db = SQLAlchemy(app)

from fortniteversus import routes