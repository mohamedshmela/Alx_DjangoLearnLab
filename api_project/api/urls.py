from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # path('books/', BookList.as_view(),name= 'book_list'),
    path('',include(router.urls))
]