import json

import my_settings
import math
from django.views import View
from django.http import JsonResponse

from users.models import User
from .models import Review
from .models import OrderItem
from .models import Order
from .models import OrderStatus


class ReviewView(View):
    def get(self, request):
        reviews = Review.objects.all()
        review_result = []
        #print(reviews)

        for review in reviews:
            review_id=Review.objects.get(id=review.id).id
            order_item_id=OrderItem.objects.get(id=review_id).id
            user_id=Order.objects.get(id=order_item_id).id
            name = User.objects.get(id=user_id).name
            birthday = User.objects.get(id=user_id).birthday

            name_l = list(name)
            name_l[1] = '*'
            name2 = "".join(name_l)
                                                   
            birthyear=birthday.year
            ages = math.floor(int(2020-birthyear))

            for review in reviews:
                review_result_dic = {
                    'rate' : Review.objects.get(id=review.id).rate,
                    'review_text' : Review.objects.get(id=review.id).review_text,
                    'writed_at' : Review.objects.get(id=review.id).writed_at,
                    'name' : name2,
                    'ages' : ages
                }
                review_result.append(review_result_dic)

            #print('확인값:'+user_id)
            #print('--------------------')
            #print(review.order_item_id)
            #print(review.rate)
            #print(review.review_text)
            #print(review.writed_at)
            #print(name)
            #print(birthday)
            
            #print(order_item_id)
            #print(user_id)
            #print(name)
            #print(birthday)
    

            #print(type(birthday))


            return JsonResponse ({"review_result" : review_result}, status=200)

