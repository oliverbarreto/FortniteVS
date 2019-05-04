from flask import Flask
import os
##from flask_sqlalchemy import SQLAlchemy



## ----------------------------------------------------------------------------
## App & Config
## ----------------------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or os.urandom(24)

##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
##db = SQLAlchemy(app)

from fortniteversus import routes