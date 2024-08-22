from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from .views import (LoginView, LogoutView)

urlpatterns = [
    path('list_books/',list_books, name= 'list_books'),
    path('library/', LibraryDetailView.as_view(), name= 'library'),

    #user views
    path('login/',LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('register/',views.register.as_view(), name='registration'),
]