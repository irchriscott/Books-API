# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Categories(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name
		
	def __str__(self):
		return self.name

class Books(models.Model):
	isbn = models.IntegerField(unique=True, blank=False, null=False)
	title = models.CharField(max_length=255, blank=False, null=False)
	author = models.CharField(max_length=255, blank=False, null=False)
	description = models.TextField(blank=True, null=True)
	publisher = models.CharField(max_length=255)
	category = models.ForeignKey(Categories)
	imageurl = models.URLField(null=False, blank=False)
	pdfurl = models.URLField(null=False, blank=False)
	detailsurl = models.URLField(null=True, blank=True)
	pages = models.IntegerField(blank=True, null=True)
	published_date = models.DateField(auto_created=True)
	
	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title

	
