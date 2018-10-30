from flask import json, jsonify
import unittest

from app.tests.v2.setup_test import InitialSetup

class TestProductsFunctions(InitialSetup):

    '''Tests whether the product was successfully edited'''
    def test_product_modified_successfully(self):
        feedback = self.app.put(
            '{}products/1'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.product_details), 
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["Message"]
        self.assertEqual(Message,"Product Sucessfully edited")
        self.assertEqual(feedback.status_code,200)

    '''Tests Authorization msg for attendant modify attempts'''
    def test_returns_no_permision_if_attendant_modifies_a_product(self):
        feedback = self.app.put(
            '{}products/1'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.product_details), 
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["Message"]
        self.assertEqual(Message,"You dont have permissions to modify a product")
        self.assertEqual(feedback.status_code,200)


    '''Tests whether the product was successfully deleted'''
    def test_product_successfully_deleted(self):
        feedback = self.app.delete(
            '{}products/1'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.product_details), 
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["Message"]
        self.assertEqual(Message,"Product Sucessfully deleted")
        self.assertEqual(feedback.status_code,200)

    '''Tests whether a message is returned if a product is not available'''
    def test_return_error_message_if_no_product_to_delete(self):
        feedback = self.app.delete(
            '{}products/23'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.product_details), 
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["Message"]
        self.assertEqual(Message,"Product Not available")
        self.assertEqual(feedback.status_code,204)
    
    '''Tests if an attendant gets error on delete'''
    def test_return_error_if_no_permission_to_delete(self):
        feedback = self.app.delete(
            '{}products/1'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.product_details), 
            content_type='application/json'
            )
        Message = json.loads(feedback.data)["Message"]
        self.assertEqual(Message,"You dont have permissions to delete this product")
        self.assertEqual(feedback.status_code,403)

    