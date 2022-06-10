from django.contrib import admin

from orders.models import Order, OrderStatus


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [o.name for o in Order._meta.get_fields()]


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [o.name for o in OrderStatus._meta.get_fields()]
