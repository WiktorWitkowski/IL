from rest_framework import serializers
from .models import Author, Post, PostChangeHistory


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "name", "description", "keywords", "url"]
        read_only_fields = ["author"]

    def validate_keywords(self, value):
        """Walidacja: minimum 3 unikalne słowa kluczowe"""
        keywords = set([key.strip() for key in value.split(",")])
        if len(keywords) < 3:
            raise serializers.ValidationError("Podaj co najmniej 3 unikalne słowa kluczowe!")
        return ", ".join(keywords)

    def validate(self, data):
        """Sprawdzenie, czy `name` nie jest jednym ze `keywords`"""
        super().validate(data)
        name = data.get("name") or getattr(self.instance, "name")
        keywords = data.get("keywords") or getattr(self.instance, "keywords")
        keywords = [key.lower().strip() for key in keywords.split(",")]
        if name.lower() in keywords:
            raise serializers.ValidationError("Nazwa nie moze być jednym ze słow kluczowych!")
        return data

    def update(self, instance, validated_data):
        if any([
            validated_data.get("name"),
            validated_data.get("description"),
            validated_data.get("keywords"),
            validated_data.get("url"),
        ]):
            PostChangeHistory.objects.create(post=instance, **validated_data)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["author"] = instance.author.ip
        return data


class PostHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostChangeHistory
        fields = "__all__"
