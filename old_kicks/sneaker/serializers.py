from dataclasses import fields
from rest_framework import serializers
from .models import Brand, Sneaker

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )


class BrandSerializer(serializers.ModelSerializer):
    sneakers = SneakerSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "sneakers"
        )
