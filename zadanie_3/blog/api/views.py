from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from .models import Post, PostChangeHistory, Author
from .permission import IsPostAuthor
from .serializers import PostSerializer, AuthorSerializer, PostHistorySerializer
from .services import get_client_ip, get_author


class PostManageViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthor,]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        ip = get_client_ip(request=self.request)
        serializer.save(author=get_author(ip=ip))


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = LimitOffsetPagination


class PostHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Zwraca historię zmian dla danego posta (po `post_id`)."""
    serializer_class = PostHistorySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return PostChangeHistory.objects.filter(post=post).order_by("-created_at")