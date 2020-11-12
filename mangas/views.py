from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import *

class IndexView(generic.ListView):
    template_name = 'mangas/index.html'
    context_object_name = 'latest_manga_list'

    def get_queryset(self):
        """Return all manga list by alphabetical """
        return Manga.objects.order_by('manga_name')

class DetailView(generic.DetailView):
	model = Manga
	template_name = 'mangas/detail.html'
	#context_object_name = 'book_list'

class BookView(generic.DetailView):
	model = Book
	template_name = 'mangas/book_detail.html'

