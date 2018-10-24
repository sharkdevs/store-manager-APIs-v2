import unittest

from app import create_app
class InitialSetup(unittest.TestCase):

    """Call the setup function to initialize items"""
    def setUp(self):
        app = create_app(config_name='testing')
        app.app_context().push()
        self.app = app.test_client()

        #set a base url
        self.base_url = "/api/v2/"

        #Define test data
        self.registration_details = {
            "userid" : 1,
            "username" : "Meshack",
            "email" : "mesharkz1@gmail.com",
            "password" : "123123",
            "role" : "admin"
        }

        self.login_details = {
            "email" : "mesharkz1@gmail.com",
            "password" : "123123"
        }

        self.product_details = {
            "product_id" : 1,
            "product_name" : "Lexus",
            "product_price" : 456000,
            "description" : "Good vehicle",
            "quantity" : 50,
            "product_image" : "image/lexus.jpg"
        }

        self.sale_order = {
            "sales_id" : 1,
            "product_id" : 1,
            "quantity" : 3,
            "sales_amount" : 450,
            "sales_date" : "4th April 2018"
        }

