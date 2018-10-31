from flask import Flask, Blueprint
from flask_restful import Api, Resource

from app.api.v2.database import Db
from app.api.v2.views import UserLogin, UserRegistration
v2 = Blueprint('bp', __name__, url_prefix='/api/v2')

app = Api(v2)

app.add_resource(UserLogin, '/auth/login')
app.add_resource(UserRegistration,'/auth/signup')
