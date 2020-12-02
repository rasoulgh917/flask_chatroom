#Import Libs
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from functools import wraps

#Initialize flask app
app = Flask(__name__)
app.config.from_object(Config) #NOTE: Change Development to Production if needed.

#Initialize SQLAlchemy
db = SQLAlchemy(app)

#Initialize flask migrate
migrate = Migrate(app, db)

#Create a tool to check the requests
def json_only(function):
    @wraps(function)
    def inner_function(*args, **kwargs):
        if not request.is_json:
            return {'error': 'JSON only!'}, 400
        return function(*args, **kwargs)
    return inner_function
from . import views
