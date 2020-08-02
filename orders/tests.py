import json

from django.test     import (
TestCase,
Client
)
from users.models    import (
User,
Gender
)
from products.models import (
Product,
Color,
ProductColor
)
from orders.models   import (
    Order,
    OrderStatus,
    OrderItem,
    OrderImage
)

class ColorItemOrderTest(TestCase):
    def setUp(self):
        Gender.objects.create(
            name = "male"
        )

        Gender.objects.create(
            name = "female"
        )

        User.objects.create(
            email          = 'test01@test.com',
            password       = '123456',
            phone_number   = '01012345678',
            birthday       = '1980-01-01',
            name           = '김삼식',
            gender_type_id = Gender.objects.get(name = "male").id
        )

        Product.objects.create(
            name        = "선물세트",
            description = "면도용품 + 기프트 카드",
        )

        Color.objects.create(
            name = "미드나이트 네이비"
        )

        ProductColor.objects.create(
            price      = "29800",
            color_id   = Color.objects.get(id=1).id,
            product_id = Product.objects.get(id=1).id
        )

        OrderStatus.objects.create(
            name = "장바구니"
        )

        OrderImage.objects.create(
            image_url          = "https://wiselyshave-cdn.s3.amazonaws.com/assets/images/items/gift_set/gift_set_navy.png",
            products_colors_id = ProductColor.objects.get(id=1).id
        )

    def tearDown(self):
        Product.objects.all().delete()
        Color.objects.all().delete()
        ProductColor.objects.all().delete()
        OrderStatus.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
        OrderImage.objects.all().delete()
        User.objects.all().delete()
        Gender.objects.all().delete()

    def test_post_colorproduct_order_success_view(self):
        client     = Client()

        header     = {
            "HTTP_Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.DbCRvyvj5ai7zxm8dwLI_zb-CNNI5jvEA9j43cWkovc"
        }

        order_info = {
            "product_id":"1",
            "color_id":"1"
        }

        response=client.post('/order/color-select',json.dumps(order_info),content_type='application/json',**header)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"Info" : [
        {
            "item_name"   : "선물세트",
            "color"       : "미드나이트 네이비",
            "price"       : "29800.00",
            "description" : "면도용품 + 기프트 카드",
            "image_url"   : "https://wiselyshave-cdn.s3.amazonaws.com/assets/images/items/gift_set/gift_set_navy.png",
            "quantity"    : 1
        },
        {
            "shipping_price" : 0,
            "discount_price" : "0.00",
            "total_price"    : "29800.00"
        }]})


class CartItemGetTest(TestCase):
    def setUp(self):
        Gender.objects.create(
            name = "male"
        )

        Gender.objects.create(
            name = "female"
        )

        User.objects.create(
            email          = 'test01@test.com',
            password       = '123456',
            phone_number   = '01012345678',
            birthday       = '1980-01-01',
            name           = '김삼식',
            gender_type_id = Gender.objects.get(name = "male").id
        )

        Product.objects.create(
            name        = "선물세트",
            description = "면도용품 + 기프트 카드"
        )

        Color.objects.create(
            name = "미드나이트 네이비"
        )

        ProductColor.objects.create(
            price      = "29800",
            color_id   = Color.objects.get(name = "미드나이트 네이비").id,
            product_id = Product.objects.get(id = 1).id
        )

        OrderStatus.objects.create(
            name = "장바구니"
        )

        OrderImage.objects.create(
            image_url          = "https://wiselyshave-cdn.s3.amazonaws.com/assets/images/items/gift_set/gift_set_navy.png",
            products_colors_id = ProductColor.objects.get(id=1).id
        )

        Order.objects.create(
            shipping_price  = 0,
            list_price      = 0,
            discount_price  = 0,
            total_price     = 0,
            order_status_id = 1,
            user_id         = User.objects.get(id=1).id
        )

        OrderItem.objects.create(
            quantity           = 1,
            discount_price     = 0,
            order_id           = Order.objects.get(id=1).id,
            products_colors_id = ProductColor.objects.get(id = 1).id
        )

        order = Order.objects.get(id=1)
        order.list_price = ProductColor.objects.get(id=OrderItem.objects.get(id=1).products_colors_id).price
        order.total_price = order.list_price - order.discount_price
        order.save()


    def tearDown(self):
        Product.objects.all().delete()
        Color.objects.all().delete()
        ProductColor.objects.all().delete()
        OrderStatus.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
        OrderImage.objects.all().delete()
        User.objects.all().delete()
        Gender.objects.all().delete()

    def test_get_cart_list_success_view(self):
        client   = Client()

        header   = {
            "HTTP_Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.DbCRvyvj5ai7zxm8dwLI_zb-CNNI5jvEA9j43cWkovc"
        }

        response = client.get('/order/cart-list',**header)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"Info" : [
        {
            "item_name"   : "선물세트",
            "color"       : "미드나이트 네이비",
            "price"       : "29800.00",
            "description" : "면도용품 + 기프트 카드",
            "image_url"   : "https://wiselyshave-cdn.s3.amazonaws.com/assets/images/items/gift_set/gift_set_navy.png",
            "quantity"    : 1
        },
        {
            "shipping_price" : "0.00",
            "discount_price" : "0.00",
            "total_price"    : "29800.00"
        }]})
