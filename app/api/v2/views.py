from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


# local imports
from app.api.v2 import validators
from app.api.v2.database import Db
from .models import UserModel, ProductModel, SalesModel


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
            return {"message": "You are not authorized to register a user"}, 401

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
        if validators.is_empty(
                [user['username'], user['email'], user['password'], user['role']]) is True:
            return {
                "message": "You cannot insert empty data or numbers here."}, 400

        """check email validity"""
        if validators.mail_validator(user['email']) is not True:
            return {"message": "Invalid email address."}, 400

        """check password validity"""
        if validators.password_validator(user['password']) is not True:
            return {
                "message": "Password must contain atleast one letter, 1 number, uppercase charecter and be at least 6 character"}, 400

        """Check whether email is already registered"""
        value = None
        value = UserModel.get_email_query(self, user['email'])
        if value != []:
            return{"message": "User email already in use"}, 400

        UserModel(
            user['username'],
            user['email'],
            user['password'],
            user['role']).creat_user()
        return{"message": "User created successfully"}, 201


class OneProduct(Resource):

    """Get a product by id"""
    @jwt_required
    def get(self, id):
        values = ProductModel.get_product_b_id(self, id)
        if values == []:
            return{"message": "That product is not in store"}, 404
        return {"products": values}, 200

    @jwt_required
    def put(self, id):
        required = reqparse.RequestParser()
        required.add_argument(
            'product_name', type=str,
            help="You should enter product name",
            required=True)
        required.add_argument(
            'product_image', type=str,
            help="You should enter product Image",
            required=True)
        required.add_argument(
            'product_price', type=str,
            help="You should enter product_price ",
            required=True)
        required.add_argument(
            'description', type=str,
            help="description is required",
            required=True)
        required.add_argument(
            'quantity', type=str,
            help="quantity is required value",
            required=True)

        data = required.parse_args()

        if get_jwt_identity() != "admin":
            return {
                "message": "You dont have permissions to modify a product"}, 401

        product = ProductModel.get_product_b_id(self, id)

        if product == []:
            return {"message": "product does not exist"}, 404

        if validators.is_empty([
            data['product_name'],
            data['product_image'],
            data['description']
        ]) is True:
            return{"message": "Empty data or pure numbers not allowed here"}, 400

        
        if validators.is_int(
                [data['product_price'], data['quantity']]) is False:
            return{"message": "price and quantity should be numbers"}, 400
        
        comparison = ProductModel.get_one_product_query(
            self, data['product_name'])
        
        if comparison != []:
            if comparison[0][0] != id:
                 return{"message": "You have another product by that name"}, 400

        ProductModel.update_product(self, id, data)
        return {"message": "product successfully updated"}, 201

    @jwt_required
    def delete(self, id):
        if get_jwt_identity() != "admin":
            return {
                "message": "You dont have permissions to delete a product"}, 401

        product = ProductModel.get_product_b_id(self, id)

        if product == []:
            return {"message": "product does not exist"}, 404

        ProductModel.delete_product(self, id)

        return {"message": "product successfully deleted"}, 200


class Products(Resource):

    """Create a product"""
    @jwt_required
    def post(self):
        if get_jwt_identity() != "admin":
            return {"message": "You are not authorized to Create a product"}, 401

        required = reqparse.RequestParser()
        required.add_argument(
            'product_name', type=str,
            help="Product name required",
            required=True)
        required.add_argument(
            'product_price', type=str,
            help="Product price required",
            required=True)
        required.add_argument(
            'description', type=str,
            help="Description required",
            required=True)
        required.add_argument(
            'quantity', type=str,
            help="Quantity required",
            required=True)
        required.add_argument(
            'product_image', type=str,
            help="Product Image url required",
            required=True)

        product = required.parse_args()
        fields = [
            product['product_name'],
            product['description'],
            product['product_image']
        ]
        fields_int = [
            product['product_price'],
            product['quantity']
        ]
        if validators.is_empty(fields) is True:
            return {
                "message": "You cannot insert empty data or numbers here."}, 400
        if validators.is_int(fields_int) is False:
            return {"message": "Quantity and price must be numbers"}, 400

        value = ProductModel.get_one_product_query(
            self, product['product_name'])
        if value != []:
            return{"message": "Product already exists"}, 400

        ProductModel(
            product['product_name'],
            product['product_price'],
            product['description'],
            product['quantity'],
            product['product_image']).create_a_product()
        return {"message": "product created successfully"}, 201

    @jwt_required
    def get(self):
        values = ProductModel.get_all_products(self)
        if values == []:
            return{"message": "You dont have products yet"}, 200
        return {"products": values}, 200


class Sales(Resource):
    @jwt_required
    def post(self):
        if get_jwt_identity() != "attendant":
            return{"message": "You are not authorised to make sales"}, 401

        required = reqparse.RequestParser()
        required.add_argument(
            'product_id', type=str,
            help="You should enter you product id to continue",
            required=True)
        required.add_argument(
            'quantity', type=str,
            help="Quantity is required",
            required=True)

        sales = required.parse_args()

        if validators.is_int(
                [sales['product_id'], sales['quantity']]) is False:
            return {"message": "The field must be numbers"}, 400

        product = ProductModel.get_product_b_id(self, sales['product_id'])

        if product == []:
            return {"message": "The product requested is not found"}, 404

        if product[0][4] < int(sales['quantity']):
            return {
                "message": "we only have {} products in store. try again".format(
                    product[0][4])}, 404

        response = None
        sale1 = SalesModel(
            sales['product_id'],
            sales['quantity'],
            product[0][2])
        response = sale1.make_a_sale()

        if response is None:
            return {"message": "could not complete sale"}, 404
        ProductModel.update_product_quantity(
            self, sales['product_id'], product[0][4] - int(sales['quantity']))
        return{"message": "sale created successfully"}

    @jwt_required
    def get(self):
        if get_jwt_identity() !="admin":
            return {"message":"You are not authorized to view sales records"},401

        values = SalesModel.get_all_sales(self)
        if values == []:
            return{"message": "You dont have sales yet"}, 404

        return {"sales": values}, 200
