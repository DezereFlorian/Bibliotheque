# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone

class Manga(models.Model):
	EN_COURS = 'KO'
	TERMINE = 'OK'
	MANGA_CHOICES = [
		(EN_COURS, 'En cours'),
		(TERMINE, 'Terminé'),
	]
	manga_name = models.CharField('Nom de la série', max_length=200)
	pub_date = models.DateField('Date de sortie de série')
	manga_end = models.CharField('Statut de la série', max_length=2, choices=MANGA_CHOICES, default=EN_COURS)
	manga_cover = models.FileField(upload_to='mangas/static/mangas', null=True, blank=True)
	manga_cover_name = models.CharField('Nom de fichier de la couverture', max_length=200, default=' ')
	def __str__(self):
		return self.manga_name
	class Meta:
		ordering = ('manga_name', )


class Book(models.Model):
	manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
	book_name = models.CharField('Nom du tome', max_length=200, default=' ', blank=True)
	book_number = models.IntegerField('Numéro du tome', default=0)
	def __str__(self):
		if self.book_name == '':
			return '%s %s' % (self.manga.manga_name, self.book_number)
		else :
			return self.book_name
	class Meta:
		ordering = ( 'book_number', )

