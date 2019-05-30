from flask import Flask, request, render_template, flash
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField
from wtforms.validators import DataRequired
import os
import json
import time



app = Flask(__name__)
app.config["SECRET_KEY"] = "chow"

login_manager = LoginManager()
login_manager.init_app(app)



@app.route('/', methods=['GET', 'POST'])
def website():
    return render_template("index.html")

@app.route('/home/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

"""Account Operation"""

@app.route('/auth/signup/', methods=['POST'])
def sign_up():
    pass

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
@app.route('/auth/signin/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        print(request.data)
        form = LoginForm()
        if form.validate_on_submit():
            # Login and validate the user.
            # user should be an instance of your `User` class
            login_user(user)
            return render_template("home.html")
        else:
            return render_template("signin.html")

@app.route('/auth/signout/', methods=['POST'])
def sign_out():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2333', debug=True)

# python server.py 