from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from .views import (LoginView, LogoutView,
                     admin_view, librarian_view, member_view,
                     add_book, delete_book, edit_book
                     )

urlpatterns = [
    path('list_books/',list_books, name= 'list_books'),
    path('library/', LibraryDetailView.as_view(), name= 'library'),

    #user views
    path('login/',LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('register/',views.register, name='registration'),

     # Role-based views URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    #adding, editing or deleting books
    path('add_book/add/', add_book, name="add_book"),
    path('edit_book/<int:pk>/edit/', edit_book, name="edit_book"),
    path('delete_book/<int:pk>/delete/', delete_book, name="delete_book"),
]