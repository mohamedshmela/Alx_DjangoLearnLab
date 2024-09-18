from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed/', UserFeedView)

urlpatterns = router.urls
