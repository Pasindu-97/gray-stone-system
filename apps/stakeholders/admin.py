from django.contrib import admin

from apps.quotations.models import Item, Quotation, Invoice
from apps.stakeholders.models import Client, Supplier, SupplierOrder
from config.admin import custom_admin_site


@admin.register(Client, site=custom_admin_site)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier, site=custom_admin_site)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(SupplierOrder, site=custom_admin_site)
class SupplierOrderAdmin(admin.ModelAdmin):
    pass


