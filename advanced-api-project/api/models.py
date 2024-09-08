from django.db import models

# the Author model describes how the Author should be
class Author(models.Model):
    name = models.CharField(max_length= 20)

# the Book model describes how the Book should be 
class Book(models.Model):
    title = models.CharField(max_length= 20)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,on_delete= models.CASCADE)
