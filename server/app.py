import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'random_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['OAUTH_CREDENTIALS'] = {
    'google': {
        'id': os.environ.get('GOOGLE_CLIENT_ID'),
        'secret': os.environ.get('GOOGLE_CLIENT_SECRET')
    }
}
db = SQLAlchemy(app)
oauth = OAuth(app)
# Register OAuth with Google
google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    authorize_kwargs=None,
    redirect_uri='http://127.0.0.1:5000/auth/callback',
    token_url='https://accounts.google.com/o/oauth2/token',
    token_params=None,
    token_kwargs=None,
    userinfo_url='https://www.googleapis.com/oauth2/v1/userinfo',
    userinfo_params=None,
    userinfo_kwargs=None,
    client_kwargs={'scope': 'openid profile email'},
)

# Import routes after app is created to avoid circular imports
from routes import *
from models import User, Message

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
    db.create_all()
