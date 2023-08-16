from django.urls import path
from .views import (
    BookCreateView,
    BookListView,
    BookGetUpdateDeleteView,
    AuthorCreateView,
    AuthorListView,
    AuthorGetUpdateDeleteView,
    CategoryCreateView,
    CategoryListView,
    CategoryGetUpdateDeleteView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from rest_framework.urlpatterns import format_suffix_patterns

schema_view = get_schema_view(
    openapi.Info(
        title="books API",
        default_version="v1",
        description="API for managing books",
        terms_of_service="http://www.example.com/terms/",
        contact=openapi.Contact(email="contact@wxample.com"),
        license=openapi.License(name="example Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = "books"

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/books/", BookCreateView.as_view(), name="book-create"),
    path("api/books/list/", BookListView.as_view(), name="book-list"),
    path(
        "api/books/<str:pk>/",
        BookGetUpdateDeleteView.as_view(),
        name="book-get-update-delete",
    ),
    path("api/authors/", AuthorCreateView.as_view(), name="author-create"),
    path("api/authors/list/", AuthorListView.as_view(), name="author-list"),
    path(
        "api/authors/<str:pk>/",
        AuthorGetUpdateDeleteView.as_view(),
        name="author-get-update-delete",
    ),
    path("api/categories/", CategoryCreateView.as_view(), name="category-create"),
    path("api/categories/list/", CategoryListView.as_view(), name="category-list"),
    path(
        "api/categories/<str:pk>/",
        CategoryGetUpdateDeleteView.as_view(),
        name="category-get-update-delete",
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
