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
        blank=False,
        null=False,
        verbose_name='картинка'
    )

    is_access = models.BooleanField(
        default=True,
        verbose_name='Доступ'
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )




    @property
    def date(self):
        return self.date_created.strftime('%H:%M %d %m %Y')


    def __str__(self):
        return f'Книга: {self.title} | Автор: {self.author.name}'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

class Basket(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата получения/сдачи')
    is_return = models.BooleanField(default=False, verbose_name='Возвращена')

    def __str__(self):
        return f'Книга для {self.user.first_name} {self.user.last_name} | Книга: {self.book}'

    @classmethod
    def create_or_update(cls, user, book_id):
        baskets = Basket.objects.filter(user=user, book_id=book_id)
        book = Book.objects.filter(id=book_id).first()

        if not baskets.exists() or baskets.latest().is_return:
            obj = Basket.objects.create(user=user, book_id=book_id, quantity=1, is_return=False)
            book.quantity -= 1
            book.is_access = bool(book.quantity)
            book.save()
            is_created = True

            return obj, is_created
        else:
            basket = baskets.latest()
            basket.is_return = False
            basket.quantity += 1
            book.quantity -= 1
            book.is_access = bool(book.quantity)
            book.save()
            basket.save()
            is_created = False

            return is_created, basket

    class Meta:
        get_latest_by = 'created_timestamp'
        verbose_name = 'книги на выдаче'
        verbose_name_plural = 'книги на выдаче'

