
import os

from flask import Flask

from . import rest

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    
    app.register_blueprint(rest.bp)

    return app
