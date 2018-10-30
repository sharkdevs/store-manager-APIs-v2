import os
from flask import Flask
from flask_jwt_extended import JWTManager

#Import configurations
from instance.config import app_config, Config

"""Function to create the app instance"""
def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)

    # add app configurations
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    #Add JWT manager
    JWTManager(app)
  
    from app.api.v2 import v2  # import the blueprint
    app.register_blueprint(v2)  # register the blueprint

    return app