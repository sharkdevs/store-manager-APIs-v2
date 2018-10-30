from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

# local imports
from app.api.v2 import validators
from app.api.v2.database import Db
from .models import UserModel


class UserLogin(Resource):
    """Required details for login"""
    required = reqparse.RequestParser()
    required.add_argument(
        'email',
        help="You should enter you email to login",
        required=True)
    required.add_argument(
        'password',
        help="Password required to continue",
        required=True)

    def generate_auth_token(self, role):
        auth_token = create_access_token(identity=role)
        return auth_token

    def post(self):
        user = self.required.parse_args()
        query = UserModel.get_login_query(
            self, user['email'], user['password'])

        # check whether field is empty
        if validators.is_empty([user['email'], user['password']]):
            return {"Message": "You cannot submit empty data"}, 400
        if validators.mail_validator(user['email']) != True:
            return {"Message": "Invalid email address"}, 400
        user = None
        user = Db().execute_select(query)
        if user is None:
            return make_response(jsonify({
                "Message": "Invalid email or password "
            }), 400)

        role = user[3]

        auth = UserLogin.generate_auth_token(self, role)

        return {"auth": auth}, 200
