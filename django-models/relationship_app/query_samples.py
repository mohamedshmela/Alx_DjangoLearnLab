from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name = author_name)
    return Book.objects.filter(author = author)

def list_all_books_in_a_library(library_name):
    library = Library.objects.get(name = library_name)
    return library.books.all()

def get_librarian(library_name):
    library = Library.objects.get(name = library_name)
    return Librarian.objects.get(library = library)