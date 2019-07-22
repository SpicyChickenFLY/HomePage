from flask import Flask, request, render_template, flash, Markup
# from flask_login import LoginManager
# from flaskext.markdown import Markdown
from flask_wtf import FlaskForm
<<<<<<< HEAD
from flask_mongoengine import MongoEngine
=======
>>>>>>> 8080ed28d158d95bd2c083a5681dd5c41b50119c
from wtforms import Form, BooleanField, StringField
from wtforms.validators import DataRequired
from flask_debugtoolbar import DebugToolbarExtension

# from markdown import markdown
import os
import json
import time


app = Flask(__name__)
# app.debug = True # toolbar debug
app.config["SECRET_KEY"] = "chow"
<<<<<<< HEAD
app.config['MONGODB_SETTINGS'] = {
    'db': 'blog',
    'host': 'mongodb://localhost/blog',
    'connect': False
}
app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']

db = MongoEngine(app)
toolbar = DebugToolbarExtension(app)
=======


# toolbar = DebugToolbarExtension(app)
>>>>>>> 8080ed28d158d95bd2c083a5681dd5c41b50119c
# login_manager = LoginManager()
# login_manager.init_app(app)

"""------App route for website------"""

@app.route('/', methods=['GET', 'POST'])
def website():
    return render_template("index.html")

@app.route('/home/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/blog/', methods=['GET', 'POST'])
def blog_list():
    print(request.args)
    '''get all blogs(id, author, datetime)'''
    with open("static/blog/blog_list.json",'r', encoding='utf-8-sig') as f:
        blog_list = reversed(json.load(f)["blog"])
    return render_template("bloglist.html", blog_list=blog_list)

@app.route('/blog/create/', methods=['GET', 'POST'])
def blog_create(): 
    if request.method == 'GET':
        return render_template("blogcreate.html")
    else:
        pass

@app.route('/blog/<int:blog_id>/')
def blog(blog_id):
    with open("static/blog/" + str(blog_id).zfill(5) + ".md",'r', encoding='utf-8-sig') as f:
        markdown_content = f.read()
    # print(markdown_content)
    # html_content = Markup(markdown(markdown_content))
    return render_template("blog.html", content=markdown_content)

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return render_template("dashboard.html")
    else:
        return render_template("dashboard.html")

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
            return render_template("home.html")
        else:
            return render_template("signin.html")

@app.route('/auth/signout/', methods=['POST'])
def sign_out():
    pass

"""------App route for client------"""
@app.route('/blackjack', methods=['POST'])
def blackjack():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2333', debug=True)

# python server.py 
