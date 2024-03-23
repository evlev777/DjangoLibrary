from django.urls import path
from .views import IndexView, BookListView, basket_add, basket_remove


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', BookListView.as_view(), name='catalog'),
    path('page/<int:page>/', BookListView.as_view(), name='paginator'),
    path('baskets/add/<int:book_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('author/<int:author_id>/', BookListView.as_view(), name='author')
]