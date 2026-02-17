from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate(self, data):
        if not data.get("title"):
            raise serializers.ValidationError({"title": "Title is required."})

        if not data.get("author"):
            raise serializers.ValidationError({"author": "Author is required."})

        return data