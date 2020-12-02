#Import os
import os

#Create a configuration object
class Config():
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

#Configure Development mode
class Development(Config):
    Debug = True

#Configure Production mode
class Production(Config):
    Debug = False