from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.PROTECT)

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library, on_delete= models.CASCADE)
    