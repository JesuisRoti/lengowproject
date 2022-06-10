from rest_framework import serializers

from orders.models import Order, OrderStatus


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ["marketplace", "lengow"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "marketplace",
            "order_status",
            "order_id",
            "order_purchase_date",
            "order_amount",
        ]

    order_status = OrderStatusSerializer()
