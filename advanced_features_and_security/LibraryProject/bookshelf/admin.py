from django.contrib import admin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author',)
    list_filter = ('author',)

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
