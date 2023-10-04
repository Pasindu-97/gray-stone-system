from rest_framework import serializers

from apps.stakeholders.models import Client, Supplier, SupplierOrder


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class SupplierOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierOrder
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")
