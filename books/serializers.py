from rest_framework import serializers
from .models import Book, Category, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
