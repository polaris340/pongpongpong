
#from rauth import OAuth1Service, OAuth2Service
from flask_oauth import OAuth
from flask import current_app, url_for, request, redirect, session

from application import app

from datetime import datetime

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config['OAUTH_CREDENTIALS']['facebook']['id'],
    consumer_secret=app.config['OAUTH_CREDENTIALS']['facebook']['secret'],
    request_token_params={'scope': 'email'}
)




