# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Categories, Books

admin.site.register(Categories)

@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
	list_display = ('isbn', 'title', 'author', 'pages', 'published_date',)
	list_filter  = ('category','author',)
	search_fields = ['title', 'isbn',]
