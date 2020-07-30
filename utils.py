import  jwt
import  json
import  requests
import  math

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings        import (
    SECRET_KEY,
    ALGORITHM
)
from users.models       import User
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

def auth_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token    = request.headers.get('Authorization', None)
            payload         = jwt.decode(access_token,SECRET_KEY['secret'],algorithm=ALGORITHM['algorithm'])
            login_user      = User.objects.get(id=payload['id'])
            request.user    = login_user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'},status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'},status=400)

        return func(self, request, *args, **kwargs)

    return wrapper

def order_item_list(user_order):
    product_color_list  = OrderItem.objects.filter(order_id=user_order.id,products_colors_id__isnull=False)
    product_size_list   = OrderItem.objects.filter(order_id=user_order.id,products_sizes_id__isnull=False)
    product_blade_list  = OrderItem.objects.filter(order_id=user_order.id,blade_products_id__isnull=False)

    color_item_list = [{
        'item_id'     : item.id,
        'product_id'  : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).id,
        'item_name'   : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).name,
        'color'       : Color.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).color_id).name,
        'price'       : ProductColor.objects.get(id=item.products_colors_id).price,
        'discount_price' : item.discount_price,
        'description' : Product.objects.get(id=ProductColor.objects.get(id=item.products_colors_id).product_id).description,
        'image_url'   : OrderImage.objects.get(products_colors_id=item.products_colors_id).image_url,
        'quantity'    : item.quantity,
        } for item in product_color_list
    ]

    size_item_list = [{
        'item_id'        : item.id,
        'product_id'     : Product.objects.get(id=ProductSize.objects.get(id=item.products_sizes_id).product_id).id,
        'item_name'      : Product.objects.get(id=ProductSize.objects.get(id=item.products_sizes_id).product_id).name,
        'size'           : Size.objects.get(id=ProductSize.objects.get(id=item.products_sizes_id).size_id).name,
        'price'          : ProductSize.objects.get(id=item.products_sizes_id).price,
        'discount_price' : item.discount_price,
        'description'    : Product.objects.get(id=ProductSize.objects.get(id=item.products_sizes_id).product_id).description,
        'image_url'      : OrderImage.objects.get(products_sizes_id=item.products_sizes_id).image_url,
        'quantity'       : item.quantity,
        } for item in product_size_list
    ]

    blade_item_list = [{
        'item_id'        : item.id,
        'product_id'     : Product.objects.get(id=BladeProduct.objects.get(id=item.blade_products_id).product_id).id,
        'item_name'      : Product.objects.get(id=BladeProduct.objects.get(id=item.blade_products_id).product_id).name,
        'price'          : BladeProduct.objects.get(id=item.blade_products_id).price,
        'discount_price' : item.discount_price,
        'description'    : Product.objects.get(id=BladeProduct.objects.get(id=item.blade_products_id).product_id).description,
        'image_url'      : OrderImage.objects.get(blade_products_id=item.blade_products_id).image_url,
        'quantity'       : item.quantity
        } for item in product_blade_list
    ]

    order_status =  [{
        'order_id'          : user_order.id,
        'shipping_price'    : user_order.shipping_price,
        'discount_price'    : user_order.discount_price,
        'total_price'       : user_order.list_price - user_order.discount_price
    }]

    item_list = color_item_list + size_item_list + blade_item_list + order_status

    return item_list


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

