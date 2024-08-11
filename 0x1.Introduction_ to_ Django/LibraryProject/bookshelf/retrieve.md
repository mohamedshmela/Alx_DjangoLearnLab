the python command used is:
all_books = Book.objects.all()
no output is seen at this point
python command for visualization of the output:
for book in all_books:
    print(book.title, book.author, book.publication_year)

expected output is:
1984 George Orwell 1949