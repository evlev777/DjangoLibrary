# Generated by Django 4.2.4 on 2024-03-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="basket",
            name="is_return",
            field=models.BooleanField(default=False, verbose_name="Возвращена"),
        ),
    ]