from django.db import models


class Author(models.Model):
    ip = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.ip


class Post(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    keywords = models.TextField(max_length=500)
    url = models.URLField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class PostChangeHistory(models.Model):
    """Przechowuje tylko zmiany."""
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1024, null=True)
    keywords = models.TextField(max_length=500, null=True)
    url = models.URLField(max_length=1024, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"History log for post: {self.post.name}"