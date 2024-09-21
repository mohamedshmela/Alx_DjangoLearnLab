from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed/', UserFeedView, basename='feed')
router.register(r'posts/<int:pk>/like/', LikePostView.as_view())
router.register(r'posts/<int:pk>/unlike/', UnlikePostView.as_view())

urlpatterns = router.urls
