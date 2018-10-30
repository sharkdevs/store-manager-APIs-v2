import unittest
from flask import json

from app.tests.v2.setup_test import InitialSetup

class TestUserRegistration(InitialSetup):

    """Test whether registraton goes successfully"""
    def test_that_a_user_was_succcessfully_registered(self):
        response = self.app.post(
            '{}auth/signup'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.registration_details), 
            content_type='application/json'
            )
        Message = json.loads(response.data)["Message"]
        self.assertEqual(Message,"User was created Sucessfully registered")
        self.assertEqual(response.status_code,201)    
        
    """Test whether it gives authorization message to attendants who want to register"""
    def test_denies_attendant_access_to_registration(self):
        response = self.app.post(
            '{}auth/signup'.format(self.base_url), 
            headers = dict(Authorization="Bearer " + self.auth_token),
            data = json.dumps(self.registration_details), 
            content_type='application/json'
            )
        Message = json.loads(response.data)["Message"]
        self.assertEqual(Message,"You dont have access rights to registration module")
        self.assertEqual(response.status_code,403)

    def test_successfull_user_login(self):
        response = self.app.post(
            '{}auth/login'.format(self.base_url), 
            data = json.dumps(self.login_details), 
            content_type='application/json'
            )
        Message = json.loads(response.data)["Message"]
        self.assertEqual(Message,"Logged In successfully")
        self.assertEqual(feedback.status_code,200)
    
    """Gives feedback on unregistered email"""
    def test_gives_error_message_if_email_is_not_registered(self):
        response = self.app.post(
            '{}auth/login'.format(self.base_url), 
            data = json.dumps({
                "email" : "shark@mesh.com",
                "password" : "wesxa"
                }), 
            content_type='application/json'
            )
        Message = json.loads(response.data)["Message"]
        self.assertEqual(Message,"shark@mesh.com is not a registered user")
        
    """Gives feedback on bad password""" 
    def test_gives_error_message_if_wrong_password_entered(self):
        response = self.app.post(
            '{}auth/login'.format(self.base_url), 
            data = json.dumps({
                "email" : "mesharkz1@gmail.com",
                "password" : "wesxa"
                }), 
            content_type='application/json'
            )
        Message = json.loads(response.data)["Message"]
        self.assertEqual(Message,"Incorrect Password")
