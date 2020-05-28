from flask import request, redirect, url_for, render_template
from FlaskApp import app
from flask_login import login_required,login_user,logout_user
from FlaskApp.models.user import User
from FlaskApp import db
from FlaskApp import login_manager


@app.route('/', methods=['GET', 'POST'])
def root():
    return redirect(url_for('login')) # '/'は, /loginへリダイレクト

# login処理
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form["username"] != None and request.form["password"] != None:
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()
            login_user(user)
            return render_template('login_test.html',username=user.username)        
    return render_template('login.html')

# ユーザ登録処理
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
        login_user(user)
        
        return render_template('success.html')


@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        logout_user()
        return redirect(url_for('login'))

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)