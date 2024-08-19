the python command is:
new_book = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
new_book.save()
no output
or we can use another command which is:
new_book = Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)
