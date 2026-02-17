from rest_framework import generics
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Book
from .serializers import BookSerializer


@method_decorator(cache_page(60), name='get')
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer