#Import Libs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

#Initialize flask app
app = Flask(__name__)
app.config.from_object(config.Development) #NOTE: Change Development to Production if needed.

#Initialize SQLAlchemy
db = SQLAlchemy(app)

#Initialize flask migrate
migrate = Migrate(app, db)