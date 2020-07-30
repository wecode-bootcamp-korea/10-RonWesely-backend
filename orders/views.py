import  json
from datetime       import datetime
from decimal        import Decimal

from django.http    import JsonResponse
from django.views   import View

from products.models    import (
    Product,
    BladeProduct,
    ProductColor,
    ProductSize,
    Color,
    Size
)
from orders.models      import (
    Order,
    OrderStatus,
    OrderItem,
    OrderImage
)
from utils              import (
    auth_decorator,
    order_item_list,
    round_up
)

class OrderColorItem(View):

    @auth_decorator
    def post(self,request):
        data    = json.loads(request.body)

        try:
            product_id       = data['product_id']
            color_id         = data['color_id']
            product_color_id = ProductColor.objects.get(
                product_id = product_id,
                color_id   = color_id
            ).id
            user_id          = request.user.id

            if not Order.objects.filter(
                user_id         = user_id,
                order_status_id = 1
            ).exists():
                Order(
                    shipping_price  = 0,
                    list_price      = 0,
                    discount_price  = 0,
                    total_price     = 0,
                    order_status_id = 1,
                    user_id         = user_id
                ).save()

            user_order   = Order.objects.get(
                user_id         = user_id,
                order_status_id = 1
            )

            if OrderItem.objects.filter(
                products_colors_id = product_color_id,
                order_id           = user_order.id
            ):
                color_product_item = OrderItem.objects.get(
                    products_colors_id = product_color_id,
                    order_id           = user_order.id
                )
                color_product_item.quantity += 1
                color_product_item.save()
                user_order.shipping_price   =  0
                user_order.list_price       += color_product_item.quantity * ProductColor.objects.get(id=color_product_item.products_colors_id).price
                user_order.save()

            else:
                OrderItem (
                    order_id            = user_order.id,
                    products_colors_id  = product_color_id,
                    quantity            = 1,
                    discount_price      = 0
                ).save()

                user_order.shipping_price   =  0
                user_order.list_price       += ProductColor.objects.get(id=product_color_id).price
                user_order.save()

            user_order_item_list = order_item_list(user_order)
            return JsonResponse({'Info':user_order_item_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Order.DoesNotExist:
            return JsonResponse({'message':'INVALID_ORDER'},status=400)

class OrderBulkItem(View):

    @auth_decorator
    def post(self,request):

        try:
            data           = json.loads(request.body)
            bulk_item_list = data['Info']
            user_id        = request.user.id

            for item in bulk_item_list:
                if not Order.objects.filter(user_id=user_id,order_status_id=1).exists():
                    Order(
                        shipping_price  = 2500,
                        list_price      = 0,
                        discount_price  = 0,
                        total_price     = 0,
                        order_status_id = 1,
                        user_id         = user_id
                    ).save()

                user_order = Order.objects.get(
                    user_id         = user_id,
                    order_status_id = 1
                )

                if item['product_id'] == '3':
                    if not OrderItem.objects.filter(
                        blade_products_id = BladeProduct.objects.get(id = 1).id,
                        order_id          = user_order.id
                    ):
                        OrderItem(
                            order_id            = user_order.id,
                            blade_products_id   = BladeProduct.objects.get(id=1).id,
                            quantity            = 0,
                            discount_price      = 0
                        ).save()

                    product_item  = OrderItem.objects.get(
                        blade_products_id = BladeProduct.objects.get(product_id = item['product_id']).id,
                        order_id          = user_order.id
                    )

                    product_item.quantity   += int(item['quantity'])
                    item_price               = float(BladeProduct.objects.get(id = product_item.blade_products_id).price)

                    if product_item.quantity == 2:
                        product_item.discount_price = product_item.quantity * item_price * 0.07
                        product_item.discount_price = round_up(product_item.discount_price,-2)
                    if product_item.quantity == 3:
                        product_item.discount_price = product_item.quantity * item_price * 0.15
                        product_item.discount_price = round_up(product_item.discount_price,-2)
                    if product_item.quantity >= 4:
                        product_item.discount_price = product_item.quantity * item_price * 0.2
                        product_item.discount_price = round_up(product_item.discount_price,-2)

                    product_item.save()
                    user_order.list_price     += product_item.quantity * BladeProduct.objects.get(id=product_item.blade_products_id).price
                    user_order.discount_price += Decimal(product_item.discount_price)

                if item['product_id'] == '4':
                    if not OrderItem.objects.filter(
                        products_sizes_id = ProductSize.objects.get(id = 1).id,
                        order_id          = user_order.id
                    ):
                        OrderItem(
                            order_id            = user_order.id,
                            products_sizes_id   = ProductSize.objects.get(id=1).id,
                            quantity            = 0,
                            discount_price      = 0
                        ).save()

                    product_item  = OrderItem.objects.get(
                        products_sizes_id = ProductSize.objects.get(id = 1).id,
                        order_id          = user_order.id
                    )

                    product_item.quantity   += int(item['quantity'])
                    item_price               = float(ProductSize.objects.get(id = product_item.products_sizes_id).price)

                    if product_item.quantity == 2:
                        product_item.discount_price = product_item.quantity * item_price * 0.07
                        product_item.discount_price = round_up(product_item.discount_price,-2)
                    if product_item.quantity == 3:
                        product_item.discount_price = product_item.quantity * item_price * 0.15
                        product_item.discount_price = round_up(product_item.discount_price,-2)
                    if product_item.quantity >= 4:
                        product_item.discount_price = product_item.quantity * item_price * 0.2
                        product_item.discount_price = round_up(product_item.discount_price,-2)

                    product_item.save()
                    user_order.list_price     += product_item.quantity * ProductSize.objects.get(id=product_item.products_sizes_id).price
                    user_order.discount_price += Decimal(product_item.discount_price)

                if item['product_id'] == '5':
                    if not OrderItem.objects.filter(
                        products_sizes_id = ProductSize.objects.get(id = 3).id,
                        order_id          = user_order.id
                    ):
                        OrderItem(
                            order_id            = user_order.id,
                            products_sizes_id   = ProductSize.objects.get(id=3).id,
                            quantity            = 0,
                            discount_price      = 0
                        ).save()

                    product_item  = OrderItem.objects.get(
                        products_sizes_id = ProductSize.objects.get(id = 3).id,
                        order_id          = user_order.id
                    )

                    product_item.quantity   += int(item['quantity'])
                    item_price               = float(ProductSize.objects.get(id = product_item.products_sizes_id).price)

                    if product_item.quantity == 2:
                        product_item.discount_price = product_item.quantity * item_price * 0.07
                        product_item.discount_price = round_up(product_item.discount_price,-2)
                    if product_item.quantity == 3:
                        product_item.discount_price = product_item.quantity * item_price * 0.15
                        product_item.discount_price = round_up(product_item.discount_price,-2)
                    if product_item.quantity >= 4:
                        product_item.discount_price = product_item.quantity * item_price * 0.2
                        product_item.discount_price = round_up(product_item.discount_price,-2)

                    product_item.save()
                    user_order.list_price       += product_item.quantity * ProductSize.objects.get(id=product_item.products_sizes_id).price
                    user_order.discount_price   += Decimal(product_item.discount_price)

                if user_order.list_price >= 15000:
                    user_order.shipping_price = 0

                user_order.save()

            user_order_item_list = order_item_list(user_order)
            return JsonResponse({'Info':user_order_item_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Order.DoesNotExist:
            return JsonResponse({'message':'INVALID_ORDER'},status=400)

class CartList(View):

    @auth_decorator
    def get(self,request):

        try:
            user_id    = request.user.id
            user_order = Order.objects.get(
                user_id         = user_id,
                order_status_id = 1
            )

            user_order_item_list = order_item_list(user_order)
            return JsonResponse({'Info':user_order_item_list}, status=200)

        except Order.DoesNotExist:
            return JsonResponse({'message':'INVALID_ORDER'},status=400)

class CheckOut(View):

    @auth_decorator
    def post(self,request):
        data    = json.loads(request.body)

        try:
            order_id        = data['order_id']
            user_id         = request.user.id
            paid_user_order = Order.objects.get(
                id = order_id,
                order_status_id = 1
            )

            paid_user_order.order_status_id = 2
            paid_user_order.ordered_at      = datetime.now()
            paid_user_order.save()

            user_order_item_list = order_item_list(paid_user_order)
            return JsonResponse({'Info':user_order_item_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Order.DoesNotExist:
            return JsonResponse({'message':'INVALID_ORDER'},status=400)
