import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db(transaction=True)
class TestPostApi:
    def test_create_post_happy_path(self, client, post_data):
        url = reverse("post-list")
        resp = client.post(url, post_data)
        assert resp.status_code == status.HTTP_201_CREATED

    def test_only_author_can_edit_post(self, client, example_post):
        url = reverse("post-detail", kwargs={"pk": example_post.id})
        payload = {"name": "Lorem Ipsum"}
        resp = client.patch(url, payload)
        assert resp.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize(
        "invalid_data, err_msg",
        [
            (
                {"keywords": "zet, zet ,zet"},
                "Podaj co najmniej 3 unikalne słowa kluczowe!"
            ),
            (
                {"name": "Zet", "keywords": "zet, cet, get"},
                "Nazwa nie moze być jednym ze słow kluczowych!",
            )
        ]
    )
    def test_post_validation(self, client, post_data, invalid_data, err_msg):
        post_data.update(invalid_data)
        url = reverse("post-list")
        resp = client.post(url, post_data)
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        errors = list(resp.json().values())
        assert err_msg in errors[0]
