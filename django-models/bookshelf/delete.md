python command is:
from bookshelf.models import Book
book = Book.objects.get(id=2)
book.delete()
no output but when trying to print all books nothing is print