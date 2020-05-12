from flask import request, redirect, url_for, render_template
from FlaskApp import app
from flask_login import login_required


@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form["username"] != None and request.form["password"] != None:
            username = request.form["username"]
            return render_template('login_test.html',username=username)        
    return render_template('login.html')

