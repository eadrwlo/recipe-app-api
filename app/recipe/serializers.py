"""
Serializers for the recipe API View
"""

from rest_framework import serializers
from core.models import Recipe, Tag


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for the recipe objects."""
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        print("instance", instance)
        print("validated_data", validated_data)
        return super().update(instance, validated_data)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe details view."""
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag"""
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
