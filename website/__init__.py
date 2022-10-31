from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'supersecret'

    # Blueprints register
    # app.register_blueprint(auth)

    CORS(app)
    return app
