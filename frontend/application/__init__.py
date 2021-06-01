from flask import flask
from flask__sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQAlchemy(app)

from application import routes