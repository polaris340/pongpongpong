"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""


from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(Form):	
    search = StringField('search', validators=[DataRequired])

class Autocomplete(Form):
	autocomplete = StringField('autocomplete', validators=[DataRequired])
