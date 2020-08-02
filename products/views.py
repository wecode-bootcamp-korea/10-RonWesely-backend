from django.http        import JsonResponse
from django.views       import View

from products.models    import (
    Category,
    Product,
    BladeProduct,
    ProductColor,
    RazorColor
)

class ProductDetail(View):

    def get(self,request,product_id):
        try:
            Product.objects.filter(id=product_id).exists()
            product       = Product.objects.get(id = product_id)
            category_name = Category.objects.prefetch_related('product_set').get(id = Product.objects.get(id = product_id).category_id).name

            if category_name == 'color products':
                product_color   = ProductColor.objects.get(product_id=product_id,color_id=1)
                price           = f'{int(product_color.price):,}'
                product_info    = [{
                    "product_name"        : product.name,
                    "product_description" : product.description,
                    "product_price"       : price
                }]
                return JsonResponse({'Info':product_info}, status=200)

            if category_name == 'blade products':
                blade_product   = BladeProduct.objects.get(product_id=product_id)
                price           = f'{int(blade_product.price):,}'
                product_info    = [{
                    "product_name"        : product.name,
                    "product_description" : product.description,
                    "product_price"       : price
                }]
                return JsonResponse({'Info':product_info}, status=200)

            if category_name == 'size products':
                prefetch_product_size   = Product.objects.prefetch_related('productsize_set').get(id=product_id)
                product_size_data       = [{
                    'product_name'     : product.name,
                    'product_price'    : f'{int(product_size.price):,}',
                    'product_size'     : product_size.size.name,
                    'size_description' : product_size.size.description
                    }for product_size in list(
                        prefetch_product_size.productsize_set.filter(skin_type_id=1)|
                        prefetch_product_size.productsize_set.filter(skin_type_id=None))]
                return JsonResponse({'Info':product_size_data},status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message':'INVALID_PRODUCT'},status=400)

class ColorDetail(View):

    def get(self,request):
        try:
            Product.objects.filter(id=1).exists()
            prefetch_product_color  = Product.objects.prefetch_related('productcolor_set').get(id=1)
            product_color_data      = [{
                'color_id'       : product_color.color.id,
                'color_name'     : product_color.color.name,
                'color_eng_name' : RazorColor.objects.get(color_id=product_color.color.id).eng_name, 
                'color_url'      : RazorColor.objects.get(color_id=product_color.color.id).image_url
                }for product_color in list(prefetch_product_color.productcolor_set.all())
            ]
            return JsonResponse({'Info':product_color_data},status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message':'INVALID_PRODUCT'},status=400)
