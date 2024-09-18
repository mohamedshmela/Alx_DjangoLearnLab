from .views import PostViewSet, CommentViewSet, UserFeedView
from django.urls import path 

urlpatterns = [
    path('posts/', PostViewSet.as_view(), name='posts'),
    path('commetns/', CommentViewSet.as_view(), name='comments'),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
]