import  json

from django.http        import JsonResponse
from django.views       import View

from products.models    import Product,BladeProduct,ProductColor,ProductSize,Color,Size
from orders.models      import Order,OrderStatus,OrderItem,OrderImage
from utils              import auth_decorator

class OrderColorItem(View):

    @auth_decorator
    def post(self,request):
        data    = json.loads(request.body)

        try:
            product_id       = data['product_id']
            color_id         = data['color_id']
            product_color_id = ProductColor.objects.get(product_id = product_id,color_id = color_id).id
            user_id          = request.user.id

            if not Order.objects.filter(user_id=user_id,order_status_id=1).exists():
                Order(
                    shipping_price  = 0,
                    list_price      = 0,
                    discount_price  = 0,
                    total_price     = 0,
                    order_status_id = 1,
                    user_id         = user_id
                ).save()

            user_order   = Order.objects.get(user_id=user_id,order_status_id=1)

            if OrderItem.objects.filter(products_colors_id=product_color_id,order_id=user_order.id):
                color_product_item          = OrderItem.objects.get(products_colors_id=product_color_id,order_id=user_order.id)
                color_product_item.quantity += 1
                color_product_item.save()
                user_order.shipping_price   =  0
                user_order.list_price       += color_product_item.quantity*ProductColor.objects.get(id=color_product_item.products_colors_id).price
                user_order.save()

            else:
                OrderItem   (
                    order_id            = user_order.id,
                    products_colors_id  = product_color_id,
                    quantity            = 1,
                    discount_price      = 0
                ).save()

                user_order.shipping_price   =  0
                user_order.list_price       += ProductColor.objects.get(id=product_color_id).price
                user_order.save()

            product_color_list  = OrderItem.objects.filter(order_id=user_order.id,products_colors_id__isnull=False)
            product_size_list   = OrderItem.objects.filter(order_id=user_order.id,products_sizes_id__isnull=False)
            product_blade_list  = OrderItem.objects.filter(order_id=user_order.id,blade_products_id__isnull=False)

            color_item_list =[{
                'item_name'     : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).name,
                'color'         : Color.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).color_id).name,
                'price'         : ProductColor.objects.get(id=item.products_colors_id).price,
                'description'   : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).description,
                'image_url'     : OrderImage.objects.get(products_colors_id=item.products_colors_id).image_url,
                'quantity'      : item.quantity,
            } for item in product_color_list]

            order_status =  [{
                'shipping_price'    : user_order.shipping_price,
                'discount_price'    : user_order.discount_price,
                'total_price'       : user_order.list_price-user_order.discount_price
            }]
            user_order_item_list = color_item_list + order_status

            return JsonResponse({'Info':user_order_item_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class CartList(View):

    @auth_decorator
    def get(self,request):

        try:
            user_id          = request.user.id
            user_order   = Order.objects.get(user_id=user_id,order_status_id=1)

            product_color_list  = OrderItem.objects.filter(order_id=user_order.id,products_colors_id__isnull=False)
            product_size_list   = OrderItem.objects.filter(order_id=user_order.id,products_sizes_id__isnull=False)
            product_blade_list  = OrderItem.objects.filter(order_id=user_order.id,blade_products_id__isnull=False)

            color_item_list = [{
                'item_name'     : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).name,
                'color'         : Color.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).color_id).name,
                'price'         : ProductColor.objects.get(id=item.products_colors_id).price,
                'description'   : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).description,
                'image_url'     : OrderImage.objects.get(products_colors_id=item.products_colors_id).image_url,
                'quantity'      : item.quantity,
            } for item in product_color_list]

            order_status =  [{
                'shipping_price'    : user_order.shipping_price,
                'discount_price'    : user_order.discount_price,
                'total_price'       : user_order.list_price-user_order.discount_price
            }]
            user_order_item_list = color_item_list + order_status

            return JsonResponse({'Info':user_order_item_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
