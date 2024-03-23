from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import Author, Book, Basket
from django.shortcuts import HttpResponseRedirect
from django.utils.timezone import now


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



@login_required
def basket_add(request, book_id):
    Basket.create_or_update(user=request.user, book_id=book_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    book = Book.objects.get(id=basket.book.id)
    book.quantity += basket.quantity
    book.is_access = True
    basket.is_return = True
    basket.created_timestamp = now()
    book.save()
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))