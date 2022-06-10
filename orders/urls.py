from django.urls import path
from rest_framework import routers

from .views import *

app_name = __package__
router = routers.DefaultRouter()

router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    path(
        "create_orders_from_api/", create_orders_from_api, name="create_orders_from_api"
    ),
] + router.urls
