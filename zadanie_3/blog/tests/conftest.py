import pytest
from rest_framework.test import APIClient

from api.models import Post, Author


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def author():
    return Author.objects.create(ip="127.0.0.2")


@pytest.fixture
def example_post(author):
    return Post.objects.create(
        name="Test 1",
        author=author,
        description="test",
        keywords="raz, dwa, trzy",
        url="https://www.example.com"
    )


@pytest.fixture
def post_data():
    return {
        "name": "Lorem Ipsum",
        "description": "foo bar",
        "keywords": "alfe, beta, gamma",
        "url": "https://www.example.com"
    }