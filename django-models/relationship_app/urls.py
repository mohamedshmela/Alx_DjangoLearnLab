from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views
from .views import (user_login, user_logout, user_register)
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    add_book, edit_book, delete_book,
    user_login, user_logout, user_register,
    admin_view, librarian_view, member_view,
    LibraryDetailView,
)

urlpatterns = [
    path('list_books/',list_books, name= 'list_books'),
    path('library/', LibraryDetailView.as_view(), name= 'library'),

    #user views
    path('login/',LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('register/',views.register.as_view(), name='registration'),
]