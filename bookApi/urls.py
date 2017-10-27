from django.conf.urls import url
from django.contrib import admin
from books import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'api/books/all/$', views.api_get_all_books, name="all_books_api" ),
	url(r'api/books/book=(?P<book_id>\d+)', views.api_get_single_book, name="single_book_api"),
	url(r'api/books/search/term=(?P<term>[^/]+)&table=(?P<table>[^/]+)', views.api_search_book, name="search_book_api")
]
