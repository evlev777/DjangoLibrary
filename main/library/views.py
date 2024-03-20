from django.views.generic import TemplateView, ListView

from .models import Author, Book


class IndexView(TemplateView):
    template_name = 'library/index.html'
    name = 'Library'


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'library/book.html'
    paginate_by = 3
    title = 'Libray - Каталог'