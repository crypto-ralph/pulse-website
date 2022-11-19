import os

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = False if os.environ.get('APP_ENV') == 'PROD' else True
    app.config['DEBUG'] = False if os.environ.get('APP_ENV') == 'PROD' else True
    app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")

    CORS(app)
    return app
