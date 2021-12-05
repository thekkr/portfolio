from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class SearchForm(FlaskForm):
    location = StringField('Location')
    submit = SubmitField('Search')
