from django.contrib import admin

from .models import Author, Book, Basket

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'quantity', 'image', 'author', 'is_access')
    prepopulated_fields = {
        'slug': ('author', 'title')
    }

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    list_display = ('book', 'user', 'created_timestamp', 'is_return', 'quantity',)
    fields = ('book', 'quantity', 'created_timestamp', 'is_return',)
    readonly_fields = ('created_timestamp',)

