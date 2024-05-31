from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
oauth = OAuth(app)

# Register OAuth providers
oauth.register(
    name='google',
    client_id='990094852031-6ar4f1080pfh02fe9juanpghbjcbriso.apps.googleusercontent.com',
    client_secret='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',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    redirect_uri='http://localhost:5000/auth/callback',
    client_kwargs={'scope': 'openid profile email'},
)

from routes import *

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
