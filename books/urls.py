from django.urls import path
from . import views
from .views import BookCreateView

urlpatterns = [
    path("/", views.books, name="books"),
    path('api/books/', BookCreateView.as_view(), name='create-book'),
]



