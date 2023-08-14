from django.urls import path
from .views import (
    BookCreateView,
    BookListView,
    BookGetDeleteView,
    AuthorCreateView,
    AuthorListView,
    AuthorGetDeleteView,
    CategoryCreateView,
    CategoryGetDeleteView,
    CategoryListView,
    UpdateAuthor,
    UpdateBook,
    UpdateCategory,
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

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/books/", BookCreateView.as_view(), name="book-create"),
    path("api/books/list/", BookListView.as_view(), name="book-list"),
    path("api/books/<uuid:uuid>/", BookGetDeleteView.as_view(), name="book-delete"),
    path("api/books/<uuid:pk>/", UpdateBook.as_view(), name="update-book"),
    path("api/authors/", AuthorCreateView.as_view(), name="author-create"),
    path("api/authors/list/", AuthorListView.as_view(), name="author-list"),
    path("api/books/<uuid:uuid>/", AuthorGetDeleteView.as_view(), name="author-delete"),
    path("api/books/<uuid:pk>/", UpdateAuthor.as_view(), name="update-author"),
    path("api/books/", CategoryCreateView.as_view(), name="category-create"),
    path("api/books/list/", CategoryListView.as_view(), name="category-list"),
    path(
        "api/books/<uuid:uuid>/",
        CategoryGetDeleteView.as_view(),
        name="category-delete",
    ),
    path("api/books/<uuid:pk>/", UpdateCategory.as_view(), name="update-category"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
