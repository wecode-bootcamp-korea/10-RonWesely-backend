from django.shortcuts import render

import json
import bcrypt
import jwt

import my_settings
from django.views import View
from django.http import JsonResponse

from .models import Users

class UserView(View):
    def get(self, request, id):
        if User.objects.filter(id=id).exitst():
            user = User.objects.get(id=id)
            return JsonResponse({"userid":users.userid}, status=200)
        return JsonResponse ({"message":"no user"}, status=400)

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Users.objects.filter(userid = data['userid']).exists():
                return JsonResponse({'message':'email_already_exists'}, status=400)

            if '@' not in data['userid']:
                return JsonResponse({'message':'invalid_email'}, status=400)

            if len(data['password']) < 6:
                return JsonResponse({'message':'at_least_6_digits_please'}, status=400)
            
            password = data['password'].encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_crypt = password_crypt.decode('utf-8')

            if len(data['phone_no']) != 11:
                return JsonResponse({'message': 'invalid_phone_number'}, status=400)
            
            phone_no = data['phone_no']

            #if type(int(data['birthday']) != int:
            #    return JsonResponse({'message':'invalid_birthday'}, status=400)

            birthyear = data['birthday'][0:2]
            if int(birthyear) > 30 :
                birthyear = '19' + birthyear
            else:
                birthyear = '20' + birthyear

            birthmonth = data['birthday'][2:4]
            birthdayday = data['birthday'][4:6]

            birthday_edit = birthyear + '-' + birthmonth + '-' + birthdayday
            
            name = data['name']
            gender = data['gender']
            #shipping_address = data['shipping_address']

            Users.objects.create(
                userid = data['userid'],
                password = password_crypt,
                phone_no = data['phone_no'],
                birthday = birthday_edit,
                name = data['name'],
                gender = data['gender'],
                #shipping_address = data['shipping_address']
            ).save()

            return JsonResponse({'message':'SUCCESS!'}, status=200)

        except KeyError:
            return JsonResponse ({'message':'INVALID_KEY'}, status=400)

class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Users.objects.filter(userid=data['userid']).exists():
                user = Users.objects.get(userid=data['userid'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'userid':data['userid']}, my_settings.SECRET_KEY['secret'], algorithm="HS256")
                    access_token = token.decode('utf-8')
                    return JsonResponse({'message' : '로그인 성공'}, user.name, status=200)

                else:
                    return JsonResponse({'Message':'Password error'}, status=400)

        except KeyError:
            return JsonResponse({'Message':'Key_error'}, status=400)

