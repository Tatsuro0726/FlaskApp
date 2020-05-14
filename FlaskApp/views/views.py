from flask import request, redirect, url_for, render_template
from FlaskApp import app
from flask_login import login_required,login_user,logout_user
from FlaskApp.models.user import User
from FlaskApp import db
from FlaskApp import login_manager


@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form["username"] != None and request.form["password"] != None:
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.get(username)
            login_user(user,True)
            return render_template('login_test.html',username=username)        
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = User(email=email, username=username, password=password)
        
        db.session.add(user)
        db.session.commit()

        login_user(user,True)
        
        return render_template('success.html')

@login_required
@app.route('/homepage', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('homepage.html')
    
    if request.method == 'POST':
        logout_user()
        return render_template('homepage.html')

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
