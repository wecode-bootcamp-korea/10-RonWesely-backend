from django.shortcuts import render

import json
import bcrypt
import jwt

import my_settings
from django.views import View
from django.http import JsonResponse

from .models import Users, Gender

#class UserView(View):
#    def get(self, request, id):
#        if User.objects.filter(id=id).exitst():
#            user = User.objects.get(id=id)
#            return JsonResponse({"userid":users.userid}, status=200)
#        return JsonResponse ({"message":"no user"}, status=400)


class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Users.objects.filter(email = data['email']).exists():
                return JsonResponse({'message': 'email_already_exists'}, status=400)

            if '@' not in data['email']:
                return JsonResponse({'message':'invalid_email'}, status=400)

            if len(data['password']) < 6:
                return JsonResponse({'message':'at_least_6_digits_please'}, status=400)
            
            password = data['password'].encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_crypt = password_crypt.decode('utf-8')

            if len(data['phone_number']) != 11:
                return JsonResponse({'message':'invalid_phone_number'}, status=400)
            
            phone_number = data['phone_number']
            birthday = data['birthday'] 
            
            #if type(int(data['birthday']) != int:
            #    return JsonResponse({'message':'invalid_birthday'}, status=400)

            birthyear = data['birthday'][0:2]
            if int(birthyear) > 30 :
                birthyear = '19' + birthyear
            else:
                birthyear = '20' + birthyear

            birthmonth = data['birthday'][2:4]
            birthdate = data['birthday'][4:6]

            birthday_edit = birthyear + '-' + birthmonth + '-' + birthdate

            Users.objects.create(
                email = data['email'],
                password = password_crypt,
                phone_number = data['phone_number'],
                birthday = birthday_edit,
                name = data['name'],
                gender_type = Gender.objects.get(name = data['gender_type'])
            ).save()

            return JsonResponse({'message':'Success!'}, status=200)

        except KeyError:
            return JsonResponse ({'message':'INVALID_KEY'}, status=400)

class SignIn_when_email_exists(View):
    def post(self, request):
        data = json.loads(request.body)

        if Users.objects.filter(email=data['email']).exists():
            user = Users.objects.get(email=data['email'])
            user_name=list(user.name)
            user_name[1] = '*'
            user_name_s = "".join(user_name)

            return JsonResponse({'name':user_name_s}, safe=False)

            
class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Users.objects.filter(email=data['email']).exists():
                user= Users.objects.get(email=data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'email':data['email']}, my_settings.SECRET_KEY['secret'], algorithm="HS256")
                    access_token = token.decode('utf-8')
                      
                    return JsonResponse({'Profile':{'name':user.name, 'email':user.email}}, status=200, safe=False)

                else:
                    return JsonResponse({'Message':'Password error'}, status=400)

        except KeyError:
            return JsonResponse({'Message':'Key_error'}, status=400)

