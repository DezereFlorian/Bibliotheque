# Generated by Django 2.0.2 on 2020-05-21 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0012_auto_20200519_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_resum',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
    ]
