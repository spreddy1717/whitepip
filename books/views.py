from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Category
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


class BookCreateView(APIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListView(APIView):
    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookGetUpdateDeleteView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AuthorCreateView(APIView):
    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorListView(APIView):
    def get(self, request, format=None):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorGetUpdateDeleteView(APIView):
    def put(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CategoryCreateView(APIView):
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryGetUpdateDeleteView(APIView):
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
