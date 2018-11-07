import unittest
from flask import json, jsonify

from app.tests.v2.setup_test import InitialSetup


class TestProductsFunctions(InitialSetup):
    '''Gives feedback if the product is out of stock'''

    def test_gives_Alert_feedback_if_product_not_in_stock(self):
        """Product out of stock feedback"""
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

    def test_return_all_sales_orders(self):
        """Returns all sale orders"""
        self.creat_product()
        self.register_attendant()
        auth_token1 = self.attendant_login()
        self.make_sale(auth_token1)
        auth_token = self.admin_login()
        response = self.app.get(
                '{}sales'.format(
                    self.base_url),
                headers=dict(
                    Authorization="Bearer " +
                    auth_token),
                content_type='application/json')
        self.assertEqual(response.status_code,200)
    def test_return_sale_orders_by_id(self):
        """Returns a sale order by id"""
        self.creat_product()
        self.register_attendant()
        auth_token1 = self.attendant_login()
        self.make_sale(auth_token1)
        auth_token = self.admin_login()
        response = self.app.get(
                '{}sales/1'.format(
                    self.base_url),
                headers=dict(
                    Authorization="Bearer " +
                    auth_token),
                content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_attendant_cant_view_sale_orders(self):
        """Attendats cant view sale orders"""
        self.creat_product()
        self.register_attendant()
        auth_token = self.attendant_login()
        self.make_sale(auth_token)
        response = self.app.get(
                '{}sales/1'.format(
                    self.base_url),
                headers=dict(
                    Authorization="Bearer " +
                    auth_token),
                content_type='application/json')
        Message  = json.loads(response.data)["message"]
        self.assertEqual(Message,"You are not authorised to view sales")
    
    def test_admin_cant_post_sales(self):
        """Deny admin sales permission"""
        auth_token = self.admin_login()
        feedback = self.app.post(
            '{}sales'.format(self.base_url),
            headers=dict(Authorization="Bearer " + auth_token),
            data=json.dumps(self.sale_order),
            content_type='application/json'
        )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message, "You are not authorised to make sales")
        self.assertEqual(feedback.status_code, 401)

    def test_attendant_can_post_sales(self):
        """Attendant can create sale order"""
        self.creat_product()
        self.register_attendant()
        auth_token = self.attendant_login()
        feedback = self.app.post(
            '{}sales'.format(self.base_url),
            headers=dict(Authorization="Bearer " + auth_token),
            data=json.dumps(self.sale_order),
            content_type='application/json'
        )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message, "sale created successfully")
        self.assertEqual(feedback.status_code, 201)

    def test_attendant_cant_sale_null_values(self):
        """Attendant cant sell 0 products"""
        self.creat_product()
        self.register_attendant()
        auth_token = self.attendant_login()
        feedback = self.app.post(
            '{}sales'.format(self.base_url),
            headers=dict(Authorization="Bearer " + auth_token),
            data=json.dumps(self.sale_order_0),
            content_type='application/json'
        )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message, "You can not sell zero quantity")
        self.assertEqual(feedback.status_code, 400)
