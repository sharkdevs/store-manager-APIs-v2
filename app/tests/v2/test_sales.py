import unittest
from flask import json, jsonify

from app.tests.v2.setup_test import InitialSetup


class TestProductsFunctions(InitialSetup):
    '''Gives feedback if the product is out of stock'''

    def test_gives_Alert_feedback_if_product_not_in_stock(self):
        self.register_attendant()
        auth_token = self.attendant_login()
        # make the quantity more than stock
        self.sale_order['quantity'] = 80
        feedback = self.app.post(
            '{}sales'.format(
                self.base_url),
            headers=dict(
                Authorization="Bearer " +
                auth_token),
            data=json.dumps(
                self.sale_order),
            content_type='application/json')
        res = json.loads(feedback.data)
        self.assertEqual(res['message'], "The product requested is not found")