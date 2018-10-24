from flask import Flask

#Import configurations
from instance.config import app_config, Config

"""Function to create the app instance"""
def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    
    app.config.from_pyfile('config.py')

   
    return app