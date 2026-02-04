from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.query_params.get('category')
        model = self.request.query_params.get('model')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        search = self.request.query_params.get('search')

        ordering = self.request.query_params.get('ordering')

        if category:
            queryset = queryset.filter(category_id=category)

        if model:
            queryset = queryset.filter(model_id=model)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if search:
            queryset = queryset.filter(title__icontains=search)

        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset