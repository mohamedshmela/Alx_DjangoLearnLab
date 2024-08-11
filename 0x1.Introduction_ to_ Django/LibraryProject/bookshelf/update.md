python command is :
single_book = Book.objects.get(id=2)
single_book.title = 'Nineteen Eighty-Four'
no output is expected 
when printing the title of the book it will show that it was successfully changed