from django.core.management import call_command
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from orders.models import Order, OrderStatus
from orders.views import OrderViewSet

ORDER_CONTENT = {
    "marketplace": "amazon",
    "order_id": "1245",
    "order_purchase_date": timezone.now().date(),
    "order_amount": 1200,
}
ORDER_STATUS_CONTENT = {
    "marketplace": "leclerc",
    "lengow": "Bonjour",
}


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        Order.objects.create(**ORDER_CONTENT)
        OrderStatus.objects.create(**ORDER_STATUS_CONTENT)

    def test_order_creation(self):
        order = Order.objects.first()
        self.assertEqual(order.marketplace, "amazon")
        self.assertEqual(order.order_id, "1245")
        self.assertIsNotNone(order.order_purchase_date)
        self.assertEqual(order.order_amount, 1200)

    def test_order_status_creation(self):
        order_status = OrderStatus.objects.first()
        self.assertEqual(order_status.marketplace, "leclerc")
        self.assertEqual(order_status.lengow, "Bonjour")

    def test_unicity_order_status(self):
        try:
            OrderStatus.objects.create(**ORDER_STATUS_CONTENT)
            return False
        except IntegrityError:
            return True

    def test_set_null(self):
        ORDER_CONTENT["order_status"] = OrderStatus.objects.first()
        order_with_os = Order.objects.create(**ORDER_CONTENT)
        self.assertEqual(Order.objects.count(), 2)
        self.assertIsNotNone(order_with_os.order_status)
        OrderStatus.objects.first().delete()
        self.assertEqual(Order.objects.count(), 2)

    def test_view_list(self):
        Order.objects.create(**ORDER_CONTENT)
        Order.objects.create(**ORDER_CONTENT)
        o = OrderViewSet()
        li = o.get_queryset()
        self.assertEqual(li.count(), 3)

    def test_view_retrieve(self):
        ORDER_CONTENT["marketplace"] = "Auchan"
        order_with_os = Order.objects.create(**ORDER_CONTENT)
        factory = APIRequestFactory()
        factory.get(f"/api/orders/{order_with_os.id}")

    def test_command(self):
        """
        We are supposing that the API will always return 5 objects.
        The correct implementation would be to create a test xml and test the command
        with this file.
        """
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderStatus.objects.count(), 1)
        args = []
        opts = {}
        call_command('create_orders_from_api', *args, **opts)
        self.assertEqual(Order.objects.count(), 6)
        self.assertEqual(Order.objects.count(), 6)
