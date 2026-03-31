from django.shortcuts import render
from .models import Category , Product 
from django.http import JsonResponse
# Create your views here.

#from django.http import scrf_exempt
import json
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
#def create_product(request):
#    if request.method == 'POST':
#        data = json.loads(request.body)
#
#        category = Category.objects.get(id = data['category_id'])

#        product = Product.objects.create(
#
#            name = data['name'],
#            price = data['price'],
#            description = data['description'],
#            count = data['count'],
#            is_active = data['is_active'],
#            category = category
#
#        )
#
#        return JsonResponse({'id': product.id})
#    return JsonResponse ({'error' : 'Only POST allowed'})




from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer , ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail= True , methods= ['get'])
    def prodcuts(self , request , pk = None):
        category = self.get_object()
        products = Category.products.all()
        serializer = ProductSerializer(products , many = True)
        return Response (serializer.data)

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer








def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    data = {
         'products': products,
        'categories' : categories,


    }

    return render (request, 'api/home.html', {

        'products': products,
        'categories' : categories,

    })


def products_html(request):
    products = Product.objects.all()
    return render(request, 'api/products.html', {'products': products})







def products_list(request):
    products = Product.objects.all()
    data = []

    for product in products:
        data.append({
            'id' : product.id,
            'name' : product.name,
            'price' : product.price,
            'description' : product.description,
            'count' : product.count,
            'is_active' : product.is_active,
            'category_id' : product.category.id,
            'category_name' : product.category.name,
        })

    return JsonResponse(data , safe = False)

def product_detail(request , id):
    try:
        product = Product.objects.get(id = id)
        data = {
            'id' : product.id,
            'name' : product.name,
            'price' : product.price,
            'description': product.description,
            'count' : product.count,
            'is_active' : product.is_active,
            'category_id' : product.category.id,   
            'category_name' : product.category.name,

        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error' : 'Product not found'}, status = 404)

def categories_list(request):
    categories = Category.objects.all()
    data = []

    for category in categories:
        data.append({
            'id' : category.id,
            'name' : category.name,
        })
    return JsonResponse(data , safe = False)

def category_detail(request , id) :
    try:
        category = Category.objects.get(id = id)
        data = {
            'id':category.id,
            'name' : category.name,
        }
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error' : 'Category not found'}, status = 404)
    
def category_products(request , id ):
    try : 
        category = Category.objects.get(id = id)
        products = category.products.all()

        data = []

        for product in products :
            data.append({
                'id' : product.id,
                'name' : product.name,
                'price' : product.price,
                'description' : product.description,
                'count' : product.count,
                'is_active' : product.is_active,
                'category_name' : category.name,



            }) 
        return JsonResponse(data , safe = False)
    except Category.DoesNotExist:
        return JsonResponse({'error' : 'Category not found'}, status = 404)