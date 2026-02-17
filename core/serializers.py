from rest_framework import serializers
from .models import Category, Models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = "__all__"