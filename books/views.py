from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import BookSerializer
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
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDeleteView(APIView):
    def delete(self, request, uuid, format=None):
        book = get_object_or_404(Book, uuid=uuid)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
