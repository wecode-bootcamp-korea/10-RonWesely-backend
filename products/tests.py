import json

from django.test    import (
    TestCase,
    Client
)

from .models        import (
    Category,
    Product,
    Color,
    ProductColor
)

class ProductTest(TestCase):
    def setUp(self):
        Category.objects.create(
            name = "color products"
        )

        Product.objects.create(
            category_id = Category.objects.get(id=1).id,
            name        = "선물세트",
            description = "면도용품 + 기프트 카드"
        )

        Color.objects.create(
            name = "미드나이트 네이비",
        )

        ProductColor.objects.create(
            price      = "29800",
            color_id   = Color.objects.get(name = "미드나이트 네이비").id,
            product_id = Product.objects.get(id = 1).id
        )

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()
        Color.objects.all().delete()
        ProductColor.objects.all().delete()

    def test_get_product_success_view(self):
        client   = Client()
        response = self.client.get('/product/1')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), {
            "Info": [{
                "product_name"        : "선물세트",
                "product_description" : "면도용품 + 기프트 카드",
                "product_price"       : "29,800"
        }]})
