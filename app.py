from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///harbinger_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from forms import Prompt


@app.route('/', methods=['GET','POST'])
def index():
	if 'user' in request.form:
		users.append(request.form['user'])
	return render_template("index.html")

@app.route('/enter_prompt/', methods=['GET','POST'])
def enter_prompt():
	form = Prompt(csrf_enabled=False)
	if form.validate_on_submit():
		prompt = form.submitted_prompt.data
		return redirect(url_for("prompt_received", prompt=prompt)) 
	return render_template("enter_prompt.html", template_form = form)
#double check route
#connect route to prompt form








if __name__ == '__main__':
        app.run(host="0.0.0.0")