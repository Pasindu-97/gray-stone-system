from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.stakeholders.models import Client, Supplier, SupplierOrder
from apps.stakeholders.serializers import SupplierSerializer, ClientSerializer, SupplierOrderSerializer


@extend_schema(tags=["item-api"])
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


@extend_schema(tags=["quotation-api"])
class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


@extend_schema(tags=["invoice-api"])
class SupplierOrderViewSet(ModelViewSet):
    queryset = SupplierOrder.objects.all()
    serializer_class = SupplierOrderSerializer
