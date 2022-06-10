from django.core import management
from django.http import HttpResponseRedirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Order
from .serializers import OrderSerializer


class OrdersResultSetPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 10


class OrderViewSet(mixins.ListModelMixin, GenericViewSet):
    authentication_classes = []
    serializer_class = OrderSerializer
    pagination_class = OrdersResultSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [o.name for o in Order._meta.get_fields()]

    def get_queryset(self):
        return Order.objects.all().distinct()

    def retrieve(self, request, pk=None):
        if not pk:
            return Response(
                data={
                    "error_details": "No order id provided",
                },
                status=500,
            )
        return Response(
            data={pk: OrderSerializer(Order.objects.get(id=pk)).data}, status=200
        )


@api_view(("GET",))
@permission_classes([AllowAny])
def create_orders_from_api(request):
    try:
        management.call_command(command_name="create_orders_from_api")
    except:
        return Response(status=500)
    return HttpResponseRedirect(redirect_to="/api/orders/")
