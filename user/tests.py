from django.test import TestCase

from .models import User 


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'phone': '09026386221',
            'password': '123'}
        User.objects.create(**self.credentials)
    
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'])


class RegisterTest(TestCase):
    def setUp(self):
        self.credentials = {
        'phone': '09026386222',
        'email': 'test1@gmail.com',
        'password': 'Mypassword777',
        'first_name': 'mehdi',
        'last_name': 'davari',
        }
        User.objects.create_user(**self.credentials)
    
    def test_register(self):
        # send register data
        response = self.client.post('/register/', self.credentials, follow=True)
        # should be register now
        self.assertTrue(response.context['user'])
