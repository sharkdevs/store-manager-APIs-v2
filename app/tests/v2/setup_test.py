import unittest
from flask import json
from app import create_app
from app.api.v2.database import Db


class InitialSetup(unittest.TestCase):

    """Call the setup function to initialize items"""

    def setUp(self):
        app = create_app(config_name='testing')
        app.app_context().push()
        self.app = app.test_client()
        with app.app_context():
            Db().destroy()
            Db().create_tables()
            Db().insert_default_test_data()

        # set a base url
        self.base_url = "/api/v2/"

        # Define test data
        self.registration_details = {
            "userid": 1,
            "username": "Meshack",
            "email": "mesharkz1@gmail.com",
            "password": "123@Sda",
            "role": "attendant"
        }

        self.login_details = {
            "email": "su@admin.com",
            "password": "admin@2018*"
        }

        self.login_attendant = {
            "email": "mesharkz1@gmail.com",
            "password": "123@Sda"
        }
        self.product_details = {
            "product_id": "1",
            "product_name": "Lexus",
            "product_price": "456000",
            "description": "Good vehicle",
            "quantity": "50",
            "product_image": "image/lexus.jpg"
        }

        self.sale_order = {
            "sales_id": 1,
            "product_id": 1,
            "quantity": 3,
            "sales_amount": 450,
            "sales_date": "4th April 2018"
        }
    def make_sale(self, auth_token):
        self.app.post(
            '{}sales'.format(self.base_url),
            headers=dict(Authorization="Bearer " + auth_token),
            data=json.dumps(self.sale_order),
            content_type='application/json'
        )

    def creat_product(self):
        auth_token = self.admin_login()
        feedback = self.app.post(
            '{}products'.format(self.base_url),
            headers=dict(Authorization="Bearer " + auth_token),
            data=json.dumps(self.product_details),
            content_type='application/json'
        )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message, "product created successfully")
        self.assertEqual(feedback.status_code, 201)

    def register_attendant(self):
        auth_token = self.admin_login()
        """Register a sample attendant"""
        self.app.post(
            '{}auth/signup'.format(self.base_url),
            headers=dict(Authorization="Bearer " + auth_token),
            data=json.dumps(self.registration_details),
            content_type='application/json'
        )

    def attendant_login(self):
        """login sample attendant"""
        feedback = self.app.post(
            '{}auth/login'.format(self.base_url),
            data=json.dumps(
                self.login_attendant),
            content_type='application/json')
        res = json.loads(feedback.data)
        auth_token = res['auth']
        return auth_token

    def admin_login(self):
        """login sample admin"""
        feedback = self.app.post(
            '{}auth/login'.format(self.base_url),
            data=json.dumps(
                self.login_details),
            content_type='application/json')
        res = json.loads(feedback.data)
        auth_token = res['auth']
        return auth_token

    """Perform a Teardown"""

    def tearDown(self):
        Db().destroy()
