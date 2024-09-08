from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 20)


class Book(models.Model):
    title = models.CharField(max_length= 20)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,on_delete= models.CASCADE)
