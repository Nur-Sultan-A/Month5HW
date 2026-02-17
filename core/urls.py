from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    ModelsListCreateAPIView,
    ModelsRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path('models/', ModelsListCreateAPIView.as_view()),
    path('models/<int:pk>/', ModelsRetrieveUpdateDestroyAPIView.as_view()),
]