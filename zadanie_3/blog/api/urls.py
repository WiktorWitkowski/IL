from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostManageViewSet, AuthorViewSet, PostHistoryViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'posts', PostManageViewSet, basename="post")

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api/posts/<int:post_id>/history-change/",
        PostHistoryViewSet.as_view({"get": "list"}),
        name="post-history",
    ),
]
