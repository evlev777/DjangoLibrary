from django.contrib import admin

from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'quantity', 'image', 'author')
    prepopulated_fields = {
        'slug': ('author', 'title')
    }