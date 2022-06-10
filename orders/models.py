from django.db import models


CORRESPONDANCE_DICT = {"order_status": "OrderStatus"}


class OrderStatus(models.Model):
    class Meta:
        unique_together = ["marketplace", "lengow"]

    marketplace = models.TextField(null=True)
    lengow = models.TextField(null=True)

    def __str__(self):
        return f'{self.lengow if self.lengow else ""}/{self.marketplace if self.marketplace else self.id}'


class Order(models.Model):
    marketplace = models.TextField()
    order_status = models.ForeignKey(
        to="OrderStatus", on_delete=models.SET_NULL, null=True
    )
    order_id = models.CharField(max_length=1200)
    order_purchase_date = models.DateField(null=True)
    order_amount = models.FloatField()
