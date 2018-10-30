from flask import Flask, Blueprint
from flask_restful import Api, Resource

v2 = Blueprint('bp', __name__, url_prefix='/api/v2')

app = Api(v2)

app.add_resource(Registration, '/auth/signup')
