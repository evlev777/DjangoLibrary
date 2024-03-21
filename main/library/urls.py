from django.urls import path
from .views import IndexView, BookListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', BookListView.as_view(), name='catalog'),
    path('author/<int:author_id>/', BookListView.as_view(), name='author')
]