from .models import Author


def get_client_ip(request):
    """Zwraca user request IP."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    return x_forwarded_for.split(",")[0] if x_forwarded_for else request.META.get("REMOTE_ADDR")


def get_author(ip):
    """Tworzy obiekt autora w DB."""
    author, _ = Author.objects.get_or_create(ip=ip)
    return author
