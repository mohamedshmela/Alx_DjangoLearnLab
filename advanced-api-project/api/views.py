from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class CustomBookListView(generics.ListApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
