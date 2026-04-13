from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import CategorySerializer, ProductSerializer
from .models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()

        if product.price >= 100:
            return Response(
                {"error": "Price >= 100 болса delete жасауға болмайды"},
                status=HTTP_400_BAD_REQUEST
            )

        return super().destroy(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(['GET'], detail=True, url_path='products', url_name='products')
    def get_products_by_category(self, request, pk=None):
        query = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data, status=HTTP_200_OK)