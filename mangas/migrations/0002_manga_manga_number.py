# Generated by Django 2.0.2 on 2019-03-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='manga_number',
            field=models.IntegerField(default=1),
        ),
    ]