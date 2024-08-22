from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import (user_login, user_logout, user_register)

urlpatterns = [
    path('list_books/',list_books, name= 'list_books'),
    path('library/', LibraryDetailView.as_view(), name= 'library'),

    #user views
    path('login/',LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('register/',views.register.as_view(), name='registration'),
]