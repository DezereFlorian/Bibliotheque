# Generated by Django 2.0.2 on 2020-05-19 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0010_manga_manga_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='manga_number',
        ),
    ]
