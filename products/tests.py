from django.test    import TestCase,Client

class ProductTest(TestCase):
    def test_get_product_success_view(self):
        client=Client()
        response=self.client.get('products/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), {
                                            "Info": [
                                                        {
                                                            "name": "선물세트",
                                                            "description": "면도용품 + 기프트 카드",
                                                            "price": "29,800"
                                                        }
                                                    ]
                                            }
                                        )


