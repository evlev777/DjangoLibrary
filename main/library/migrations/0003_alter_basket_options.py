# Generated by Django 4.2.4 on 2024-03-23 18:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0002_basket_is_return"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="basket",
            options={
                "get_latest_by": "created_timestamp",
                "verbose_name": "книги на выдаче",
                "verbose_name_plural": "книги на выдаче",
            },
        ),
    ]
