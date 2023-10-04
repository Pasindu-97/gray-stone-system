from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.quotations.models import Item, Quotation, Invoice
from apps.quotations.serializers import ItemSerializer, QuotationSerializer, InvoiceSerializer


@extend_schema(tags=["item-api"])
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@extend_schema(tags=["quotation-api"])
class QuotationViewSet(ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


@extend_schema(tags=["invoice-api"])
class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
