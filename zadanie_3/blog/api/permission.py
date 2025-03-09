from rest_framework.permissions import BasePermission
from .models import Post
from .services import get_client_ip


class IsPostAuthor(BasePermission):
    """Pozwala na edycję/usunięcie posta tylko jego autorowi (po IP)."""

    def has_object_permission(self, request, view, obj: Post) -> bool:
        if request.method in ["GET", "OPTIONS"]:
            return True

        user_ip = get_client_ip(request)
        return obj.author.ip == user_ip
