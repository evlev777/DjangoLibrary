from django.db import models
from django.utils.timezone import now

class Author(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Автор'
    )

    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор',
        verbose_name_plural = 'авторы'

class Book(models.Model):
    title = models.CharField(
        max_length=258,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Книга'
    )

    slug = models.SlugField(
        max_length=258,
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        blank=False,
        null=False,
        verbose_name='количество экземпляров'
    )

    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='book_images',
        blank=True,
        null=True,
        verbose_name='картинка'
    )

    def __str__(self):
        return f'Книга: {self.title} | Автор: {self.author.name}'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'



