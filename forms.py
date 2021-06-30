from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserRegForm(FlaskForm):
  first_name = StringField("First name")
  last_name = StringField("Last name")
  submit_field = SubmitField("Register!")

class Prompt(FlaskForm):
  submitted_prompt = StringField("Please Enter Prompt: ", validators=[DataRequired()])
  submit_field = SubmitField("Generate story!")