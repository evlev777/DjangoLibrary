from django.views.generic import TemplateView, ListView

from .models import Author, Book


class IndexView(TemplateView):
    template_name = 'library/index.html'
    name = 'Library'


class BookListView(ListView):
    model = Book
    template_name = 'library/products.html'
    paginate_by = 3
    title = 'Libray - Каталог'


    def get_queryset(self, author_id=None):
        queryset = super(BookListView, self).get_queryset()
        author_id = self.kwargs.get('author_id')
        return queryset.filter(author_id=author_id) if author_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data()
        context['authors'] = Author.objects.all()
        return context