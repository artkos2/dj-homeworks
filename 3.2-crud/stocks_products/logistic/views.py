from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [ SearchFilter]
    search_fields = ['description',]

    def post(self, request):

        Product.objects.create(title = request.data['title'], description = request.data['description'])
        return Response({'Response': 'Добавлено'})

    def patch(self, request, pk):
        Product.objects.filter(id = pk).update(description = request.data['description'])
        return Response({'Response': 'Изменено'})

    def delete(self, pk):
        Product.objects.get(id=pk).delete()
        return Response({'Response': 'Удалено'})

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all() 
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['products__id',]
    pagination_class = LimitOffsetPagination
