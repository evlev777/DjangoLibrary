from django.urls import path
from .views import IndexView, BookListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('book/', BookListView.as_view(), name='book')
]