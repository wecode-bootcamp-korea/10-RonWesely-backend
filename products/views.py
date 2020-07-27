from django.http        import JsonResponse
from django.views       import View

from products.models    import Product,BladeProduct,ProductColor,ProductSize

class ProductDetail(View):

    def get(self,request,product_id):
        try:
            product = Product.objects.get(id=product_id)

            if product_id >= 1 and product_id < 3:
                product_color   = ProductColor.objects.get(product_id=product_id,color_id=1)
                price           = f'{int(product_color.price):,}'
                product_info    =   [{
                                        "name"        : product.name,
                                        "description" : product.description,
                                        "price"       : price
                                    }]
                return JsonResponse({'Info':product_info}, status=200)

            if product_id == 3:
                blade_product   = BladeProduct.objects.get(product_id=product_id)
                price           = f'{int(blade_product.price):,}'
                product_info    =   [{
                                        "name"        : product.name,
                                        "description" : product.description,
                                        "price"       : price
                                    }]
                return JsonResponse({'Info':product_info}, status=200)

            if product_id >= 4 and product_id < 6:
                prefetch_product_size   = Product.objects.prefetch_related('productsize_set').get(id=product_id)
                product_size_data       =   [{
                                                'product_name'     : product.name,
                                                'product_size'     : product_size.size.name,
                                                'product_price'    : f'{int(product_size.price):,}',
                                                'size_description' : product_size.size.description
                                            } for product_size
                                            in list(prefetch_product_size.productsize_set.filter(skin_type_id=1)|prefetch_product_size.productsize_set.filter(skin_type_id=None))]
                return JsonResponse({'Info':product_size_data},status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message':'INVALID_PRODUCT'},status=400)
