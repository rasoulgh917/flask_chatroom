#Import Libs
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from .app import db

#Create Tables

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(32), unique = True, nullable = False)
    first_name = Column(String(128), unique = False, nullable = True)
    last_name = Column(String(128), unique = False, nullable = True)
    email = Column(String(256), unique = True, nullable = False)
    password = Column(String(128), unique = False, nullable = False)
    role = Column(Integer(), unique = False, nullable = False, default = 0) # 0 -> normal , 1 -> admin

class Privacy(db.Model):
    __tablename__ = 'privacy_settings'
    id = Column(Integer(), primary_key = True)
    username = Column(String(32), unique = True, nullable = False)
    password = Column(String(128), unique = False, nullable = False)
    email_shown = Column(BOOLEAN(), unique = False , nullable = False, default = False)
    email_whitelist = Column(Text(), unique = False, nullable = True)
    email_blacklist = Column(Text(), unique = False, nullable = True)

#Create function to generate password hash
def generate_hash(password):
    if len(password) < 8:
        raise ValueError
    return generate_password_hash(password)

#Create function to check password hash
def check_hash(password_hash, password):
    return check_password_hash(password_hash, password)