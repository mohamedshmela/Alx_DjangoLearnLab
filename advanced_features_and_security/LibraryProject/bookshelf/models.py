from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view','can_view'),
            ('can_create', 'can_create'),
            ('can_edit', 'can_edit'),
            ('can_delete', 'can_delete'),
        ]


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()


class CustomUserManager(BaseUserManager):
    def create_user(self):
        pass

    def create_superuser(self):
        pass
