# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.http import HttpResponse
from books.models import Books, Categories
import datetime
import json

	
def api_get_all_books(request):
	books = (Books.objects.all().values('id', 'title', 'author', 'category__name', 'isbn', 'imageurl', 'pdfurl', 'publisher', 'description', 'detailsurl', 'pages', 'published_date'))
	#books = serializers.serialize('json', books)
	books = json.dumps(list(books), indent=4, sort_keys=True, default=str)
	return HttpResponse(books, content_type="application/json")

def api_get_single_book(request, book_id):
	book = (Books.objects.filter(pk=book_id).values('id', 'title', 'author', 'category__name', 'isbn', 'imageurl', 'pdfurl', 'publisher', 'description', 'detailsurl', 'pages', 'published_date'))
	book = json.dumps(list(book), indent=4, sort_keys=True, default=str)
	return HttpResponse(book, content_type="application/json")

def api_search_book(request, table, term):
	books = {}
	if table == "title":
		books = (Books.objects.filter(title__contains=term).values('id', 'title', 'author', 'category__name', 'isbn', 'imageurl', 'pdfurl', 'publisher', 'description', 'detailsurl', 'pages', 'published_date'))
		books = json.dumps(list(books), indent=4, sort_keys=True, default=str)
	elif table == "isbn":
		books = (Books.objects.filter(isbn__contains).values('id', 'title', 'author', 'category__name', 'isbn', 'imageurl', 'pdfurl', 'publisher', 'description', 'detailsurl', 'pages', 'published_date'))
		books = json.dumps(list(books), indent=4, sort_keys=True, default=str)
	elif table == "author":
		books = (Books.objects.filter(author__contains=term).values('id', 'title', 'author', 'category__name', 'isbn', 'imageurl', 'pdfurl', 'publisher', 'description', 'detailsurl', 'pages', 'published_date'))
		books = json.dumps(list(books), indent=4, sort_keys=True, default=str)
	return HttpResponse(books, content_type="application/json")