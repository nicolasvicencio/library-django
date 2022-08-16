from django.urls import path
from . import views

urlpatterns = [
		path('', views.home, name='home'),
		path('about', views.about, name='about'),
		path('books', views.books, name='books'),
		path('books/create', views.createBook, name='create'),
		path('books/edit', views.editBook, name='edit')
]

