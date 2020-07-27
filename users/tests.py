import json
import bcrypt

from .models import User, Gender #Path_result, Path, Shipping
from django.test import TestCase
from django.test import Client
from unittest.mock import patch, MagicMock


class SignUpTest(TestCase):
    def setUp(self):
        Gender.objects.create (
            name = '여자'
        )
        
        Gender.objects.create (
            name = '남자'
        )

        User.objects.create (
            email = 'alex@gmail.com',
            password = 'yougogirlalex',
            phone_number = '01023456789',
            birthday = '1990-03-02',
            name = 'Alex',
            gender_type = Gender.objects.get(id=1)
        )

        User.objects.create(
            email = 'alexa@gmail.com',
            password = 'yougogirlalex',
            phone_number = '01001000100',
            birthday = '1990-02-06',
            name = 'Alexa',
            gender_type = Gender.objects.get(id=2)
        )

    def tearDown(self):
        User.objects.all().delete()
        Gender.objects.all().delete()

    def test_signup_post_success(self):
        client = Client()
        user = {
            'email' : 'alex2@gmail.com',
            'password' : 'yougogirlalex',
            'phone_number' : '01023456789',
            'birthday' : '900302',
            'name' : 'Alex',
            'gender_type' : '여자'
        }
        response = client.post('/users/SignUp', json.dumps(user), content_type='applictaion/json')

        self.assertEqual(response.status_code, 200)

#    def test_signup_post_duplicated_name(self):
#        client=Client()
#        user = {
#            'email' : 'alex@gmail.com',
#            'password' : 'yougogirlalex',
#            'phone_number' : '01023456789',
#            'birthday' : '900302',
#            'name' : 'Alex',
#            'gender_type': '여자'
#        }
#        response = client.post('/users/SignUp', json.dumps(user), content_type='text/html')
#
#        self.assertEqual(response.status_code, 400)
#        self.assertEqual(response.json(),
#            {
#                'message': 'email_already_exists'
#            }
#        )

#    def test_signup_post_invalid_key(self):
#        client=Client()
#        user = {
#            'e-mail' : 'alex@gmail.com',
#            'pass-word' : 'yougogirlalex',
#            'phone-number' : '01023456789',
#            'birth-day' : '900302',
#            'na-me' : 'Alex',
#        }
#        reponse = client.post('/user/SignUp', json.dumps(user), content_type='application/json')
#
#        self.assertEqual(response.status_code, 400)
#        self.assertEqual(response.json(),
#            {
#                'message':'INVALID_KEYS'
#            }
#        )

#class SignInTest(TestCase):
#    def setUp(self):
#        client = Client()
#        Users.objects.create(
#            id = 1,
#            email = 'alex@gmail.com',
#            password = 'yougogirlalex',
#            phone_number = '01023456789',
#            birthday = '900206',
#            name = 'Alex',
#        )
#
#        Users.objects.create(
#            id = 2,
#            email = 'alex2@gmail.com',
#            password = 'yougogirlalex', 
#            phone_number = '01023456789',
#            birthday = '900206',
#            name = 'Alex',
#        )
#
#    def tearDown(self):
#        User.objects.all().delete()
#
#    def test_signin_get_success(self):
#        client = Client()
#        reponse = client.get('/user/SignIn/alex@gmail.com')
#        self.assertEqual(response.json(),
#            {
#                'users':[{'user':1}, {'user':2}]
#            }
#        )
#        self.assertEqual(response.status_code, 200)
#
#    def test_signin_get_fail(self):
#        client = Client()
#        reponse = client.get('/user/SignIn/alice@gmail.com')
#        self.assertEqual(response.json(),
#            {
#                'message': 'NO_USER'
#            }
#        )
#        self.assertEqual(response.status_code, 400)
#
#    def test_signin_get_not_found(self):
#        client = Client()
#        response = client.get('/user/SignIn?user=alex@gmail.com')
#        self.assertEqual(response.status_code, 404)
#
#
#
#
#
#
#
#
#
## Create your tests here.
