from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import (user_login, user_logout, user_register)

urlpatterns = [
    path('list_books/',list_books, name= 'list_books'),
    path('library/', LibraryDetailView.as_view(), name= 'library'),
    path('login/',user_login, name='user_login'),
    path('logout/',user_logout, name='user_logout'),
    path('register/',user_register, name='user_registration'),
]