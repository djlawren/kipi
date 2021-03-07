
import os

from flask import Flask

from . import mine, kipi

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    
    mine.MinecraftProcess.start_server()

    app.register_blueprint(kipi.bp)

    return app
