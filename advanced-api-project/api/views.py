from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer




class ListView(generics.ListApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


