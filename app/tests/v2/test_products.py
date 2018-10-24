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