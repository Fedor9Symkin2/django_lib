from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    Template_name = 'book_list.html'



