from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app\templates\list_books.html',context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app\templates\library_detail.html'
    context_object_name = 'library'
