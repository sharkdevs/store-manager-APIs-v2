from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


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

        user = Db().execute_select(query)
        if user == []:
            return make_response(jsonify({
                "Message": "Invalid email or password "
            }), 400)
        else:
            role = user[0][4]

            auth = UserLogin.generate_auth_token(self, role)

        return {"auth": auth}, 200
class UserRegistration(Resource):
    @jwt_required
    def post(self):
        if get_jwt_identity() != "admin": 
            return {"message":"You are not authorized to register a user"},401

        required = reqparse.RequestParser()
        required.add_argument(
            'email', type=str,
            help="You should enter you email to Register",
            required=True)
        required.add_argument(
            'password', type=str,
            help="Password required to continue",
            required=True)  
        required.add_argument(
            'username', type=str,
            help="You should enter your Username ",
            required=True)
        required.add_argument(
            'role', type=str,
            help="Role required to continue",
            required=True)
        
        user = required.parse_args()
        """Check for empty data"""
        if validators.is_empty([user['username'],user['email'],user['password'],user['role']]) is True:
            return {"message":"You cannot Insert empty data."},400
        
        """check email validity"""
        if validators.mail_validator(user['email']) is not True:
            return {"message":"Invalid email address."},400

        """check password validity"""
        if validators.password_validator(user['password']) is not True:
            return {"message":"Password must contain atleast one letter, 1 number, uppercase charecter and be at least 6 character"},400

        """Check whether email is already registered"""
        value = None
        value = UserModel.get_email_query(self,user['email'])
        if value is not None:
            return{"message": "User email already in use"},400

        user1 = UserModel(user['username'],user['email'],user['password'],user['role']).creat_user()
        return{"message": "User created successfully"},201
