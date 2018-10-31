from flask import json, jsonify
import unittest

from app.tests.v2.setup_test import InitialSetup

class TestProductsFunctions(InitialSetup):
    '''Gives feedback if the product isout of stock'''

    # def test_gives_Alert_feedback_if_product_not_in_stock(self):
    #     auth_token = self.admin_login()
    #     # make the quantity more than stock
    #     self.sale_order['quantity'] = 80
    #     feedback = self.app.post(
    #         '{}sales'.format(
    #             self.base_url),
    #         headers=dict(
    #             Authorization="Bearer " +
    #             auth_token),
    #         data=json.dumps(
    #             self.sale_order),
    #         content_type='application/json')
    #     res = json.loads(feedback.data)
    #     self.assertEqual(res['message'], "Product requested not in store")

    '''Tests whether the product was successfully edited'''
    # def test_product_modified_successfully(self):
    #     feedback = self.app.put(
    #         '{}products/1'.format(self.base_url),
    #         headers = dict(Authorization="Bearer " + self.auth_token),
    #         data = json.dumps(self.product_details),
    #         content_type='application/json'
    #         )
    #     Message = json.loads(feedback.data)["Message"]
    #     self.assertEqual(Message,"Product Sucessfully edited")
    #     self.assertEqual(feedback.status_code,200)

    '''Tests whether the product was successfully edited'''
    def test_product_created_successfully(self):
        
        auth_token = self.admin_login()
        feedback = self.app.post(
            '{}products'.format(self.base_url),
            headers = dict(Authorization="Bearer " + auth_token),
            data = json.dumps(self.product_details),
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message,"product created successfully")
        self.assertEqual(feedback.status_code,201)

        '''Tests Authorization msg for attendant create product attempts'''
    def test_returns_no_permision_if_attendant_creates_a_product(self):
        """Create and login an attendant"""
        self.register_attendant()
        auth_token = self.attendant_login()
        feedback = self.app.post(
            '{}products'.format(self.base_url),
            headers = dict(Authorization="Bearer " + auth_token),
            data = json.dumps(self.product_details),
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message,"You are not authorized to Create a product")
        self.assertEqual(feedback.status_code,401)

    # '''Tests Authorization msg for attendant modify attempts'''
    # def test_returns_no_permision_if_attendant_modifies_a_product(self):
    #     """Create and login an attendant"""
    #     self.register_attendant()
    #     auth_token = self.attendant_login()

        
    #     feedback = self.app.put(
    #         '{}products/1'.format(self.base_url),
    #         headers = dict(Authorization="Bearer " + auth_token),
    #         data = json.dumps(self.product_details),
    #         content_type='application/json'
    #         )
    #     Message = json.loads(feedback.data)["Message"]
    #     self.assertEqual(Message,"You dont have permissions to modify a product")
    #     self.assertEqual(feedback.status_code,200)


    # '''Tests whether the product was successfully deleted'''
    # def test_product_successfully_deleted(self):
    #     feedback = self.app.delete(
    #         '{}products/1'.format(self.base_url),
    #         headers = dict(Authorization="Bearer " + self.auth_token),
    #         data = json.dumps(self.product_details),
    #         content_type='application/json'
    #         )
    #     Message = json.loads(feedback.data)["Message"]
    #     self.assertEqual(Message,"Product Sucessfully deleted")
    #     self.assertEqual(feedback.status_code,200)

    '''Tests whether a message is returned if a product is not available'''
    def test_return_error_message_if_no_product(self):
        auth_token = self.admin_login()
        feedback = self.app.get(
            '{}products/20003'.format(self.base_url),
            headers = dict(Authorization="Bearer " + auth_token),
            data = json.dumps(self.product_details),
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["message"]
        self.assertEqual(Message,"That product is not in store")
        self.assertEqual(feedback.status_code,404)

    # '''Tests if an attendant gets error on delete'''
    # def test_return_error_if_no_permission_to_delete(self):
    #     feedback = self.app.delete(
    #         '{}products/1'.format(self.base_url),
    #         headers = dict(Authorization="Bearer " + self.auth_token),
    #         data = json.dumps(self.product_details),
    #         content_type='application/json'
    #         )
    #     Message = json.loads(feedback.data)["Message"]
    #     self.assertEqual(Message,"You dont have permissions to delete this product")
    #     self.assertEqual(feedback.status_code,403)
