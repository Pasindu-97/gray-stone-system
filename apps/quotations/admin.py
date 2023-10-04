from django.contrib import admin

from apps.quotations.models import Item, Quotation, Invoice, QuotationItem
from config.admin import custom_admin_site


@admin.register(Item, site=custom_admin_site)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Quotation, site=custom_admin_site)
class QuotationAdmin(admin.ModelAdmin):
    pass

@admin.register(QuotationItem, site=custom_admin_site)
class QuotationItemAdmin(admin.ModelAdmin):
    pass
@admin.register(Invoice, site=custom_admin_site)
class InvoiceAdmin(admin.ModelAdmin):
    pass


