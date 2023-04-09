# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField

class MovieForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpeg', 'png'], 'Images only!')])



