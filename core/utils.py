import jwt
import json

from users.models import User
from my_settings import SECRET_KEY
from my_settings import ALGORITHM
from django.http import HttpResponse, JsonResponse

class LoginConfirm:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        access_token = request.headers.get("Authorization", None)   
        try:
            if access_token:
                token_payload = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                user = User.objects.get(id=token_payload['user_id'])
                request.user = user
                return self.func(self, request, *args, **kwargs)

            return JsonResponse({'message':'NEED_LOGIN'}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'EXPIRED_TOKEN'}, status=401)

        except jwt.DecodeError:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

