from rest_framework import serializers
from .models import Order, OrderProduct
from sneaker.serializers import SneakerSerializer


class UserOrderProductSerializer(serializers.ModelSerializer):
    sneaker = SneakerSerializer()

    class Meta:
        model = OrderProduct
        fields = (
            "price",
            "sneaker",
            "quantity"
        )


class UserOrderSerializer(serializers.ModelSerializer):
    items = UserOrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "firstname",
            "lastname",
            "address",
            "city",
            "state",
            "zipcode",
            "email",
            "phonenumber",
            "stripe_token",
            "items",
            "amount_paid"
        )


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = (
            "price",
            "sneaker",
            "quantity"
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "firstname",
            "lastname",
            "address",
            "city",
            "state",
            "zipcode",
            "email",
            "phonenumber",
            "stripe_token",
            "items",
        )

    def create(self, validated_data):
        data_for_items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in data_for_items:
            OrderProduct.objects.create(order=order, **item)
        return order
