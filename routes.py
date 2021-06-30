from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import app, forms

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