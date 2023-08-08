from django.http import HttpResponse
from django.template import loader


def books(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
