from django.urls import path
from .views import BookCreateView, BookListView, BookDeleteView
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
    path("api/books/<uuid:uuid>/", BookDeleteView.as_view(), name="book-delete"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
