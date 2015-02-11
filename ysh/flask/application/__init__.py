'''
initalize Flask app
'''
from flask import Flask
import os
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.debug import DebuggedApplication
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('application')
db = SQLAlchemy(app)
app.config.from_object('config')

app.config['OAUTH_CREDENTIALS'] =   {
    'facebook': {
            'id': '766100996799677',
        'secret': '613f5d088e7082ae89435a1f9c930a80'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}
# Pull in URL dispatch routes
from application import urls
from application import views, models, forms

