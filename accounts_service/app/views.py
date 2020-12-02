#Import Libs
from .app import app, json_only, db
from flask import request
from .models import User, generate_hash, check_hash
from sqlalchemy.exc import IntegrityError
from 000

#Set route for user register
@app.route('/users/', methods = ['POST'])
@json_only
def register_user():
    #Get request args
    args = request.get_json()
    
    #Create user in database
    user = User()
    try:
        user.username = args['username']
        user.email = args['email']
        user.first_name = args['first_name']
        user.last_name = args['last_name']
        try:
            user.password = generate_hash(args['password']) 
        except ValueError:
            return {"error": "Password must be at least 8 characters"}, 406
    except KeyError:
        return {"error" : "Bad Request"}, 400
    db.session.add(user)
    try:
        db.session.commit()
        return {"error": "User added"}, 201
    except IntegrityError:
        db.session.rollback()
        return {"error": "User exists"}, 409

#Set route for user login and authorization
@app.route('/auth/', methods = ['POST'])
@json_only
def login_user():
    #Get request args
    args = request.get_json()
    try:
        username = ags['username']
        password = args['username']
    except KeyError:
        return {'error': 'Invalid request data. Please check the docs.'}, 400
    
    #Look for user in database
    user = User.query.filter(User.username.ilike(username)).first()
    if not user:
        return {'error': 'User does not exist.'}, 404
    
    #Check the password
    if not check_hash(user.password, password):
        return {"error": "Incorrect password"}, 401

    return {"info": "Logged in successfuly"}, 204