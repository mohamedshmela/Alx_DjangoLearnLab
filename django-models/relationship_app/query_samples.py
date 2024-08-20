from relationship_app.models import Author, Book

def get_books_by_author(authorName):
    author = Author.objects.get(name = authorName)
    return Book.objects.filter(author = author)