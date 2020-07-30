import json
import bcrypt
import jwt
import datetime

import my_settings
from django.views import View
from django.http import JsonResponse

from .models import User
from .models import Gender

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if '@' not in data['email']:
                return JsonResponse({'message':'invalid_email'}, status=400)

            if len(data['password']) < 6:
                return JsonResponse({'message':'at_least_6_digits_please'}, status=400)
            
            password = data['password'].encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_crypt = password_crypt.decode('utf-8')

            if len(data['phone_number']) < 10:
                return JsonResponse({'message':'invalid_phone_number'}, status=400)
            phone_number = data['phone_number']

            birthday = data['birthday'] 
            birthyear = data['birthday'][0:2]
            if int(birthyear) > 30 :
                birthyear = '19' + birthyear
            else:
                birthyear = '20' + birthyear

            birthmonth = data['birthday'][2:4]
            birthdate = data['birthday'][4:6]
            birthday_edit = birthyear + '-' + birthmonth + '-' + birthdate

            User.objects.create(
               email        = data['email'],
               password     = password_crypt,
               phone_number = data['phone_number'],
               birthday     = birthday_edit,
               name         = data['name'],
               gender_type  = Gender.objects.get(name = data['gender_type'])
            ).save()

            return JsonResponse({'message':'Success!'}, status=200)

        except KeyError:
            return JsonResponse ({'message':'INVALID_KEY'}, status=400)

class SignInWhenEmailExists(View):
    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(email=data['email']).exists():
<<<<<<< HEAD
            user         = User.objects.get(email=data['email'])
            user_name    = list(user.name)
            user_name[1] = '*'
            user_name_s  = "".join(user_name)
            print(user_name_s)

            return JsonResponse({'name':user_name_s}, safe=False, status=200)
=======
            user         = Users.objects.get(email=data['email'])
            user_name    = list(user.name)
            user_name[1] = '*'
            user_name_s  = "".join(user_name)

            return JsonResponse({'name':user_name_s}, safe=False)
>>>>>>> master

            
class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'email':data['email']}, my_settings.SECRET_KEY['secret'], my_settings.ALGORITHM['algorithm'])
                    access_token = token.decode('utf-8')
                      
                    return JsonResponse({'Access_Token':access_token})

                else:
                    return JsonResponse({'Message':'Password error'}, status=400)

        except KeyError:
            return JsonResponse({'Message':'KEY_ERROR'}, status=400)

class MyPage(View):
    def get(self, request):
        access_token = request.headers.get('Authorization', None)
        access_token_d = jwt.decode(access_token, my_settings.SECRET_KEY['secret'], my_settings.ALGORITHM['algorithm'])

        if not User.objects.filter(email = access_token_d['email']).exists():
            return JsonResponse({'message': 'INVALID_USER'})

        email = User.objects.get(email=access_token_d['email']).email
        name = User.objects.get(email=access_token_d['email']).name

        return JsonResponse({'email': email, 'name': name}, status=200)




