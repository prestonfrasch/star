from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///harbinger_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserRegForm(FlaskForm):
	first_name = StringField("First name")
	last_name = StringField("Last name")
	submit_field = SubmitField("Register!")

@app.route('/', methods=['GET','POST'])
def index():
	if 'user' in request.form:
		users.append(request.form['user'])
	return render_template("index.html")
if __name__ == '__main__':
        app.run(host="0.0.0.0")
