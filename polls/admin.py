from django.contrib import admin

from .models import *
from mangas.models import Manga, Book

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Manga)
admin.site.register(Book)