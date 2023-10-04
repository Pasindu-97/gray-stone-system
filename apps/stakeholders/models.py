from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from apps.quotations.models import Item


class Client(TimeStampedModel, models.Model):
    name = models.CharField(_("Name"), max_length=127)
    address = models.CharField(_("Address"), max_length=1023)
    contact_no = models.CharField(_("Contact Number"), max_length=15)
    completed_projects = models.IntegerField(_("Completed Projects"), default=0)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return str(self.id)


class Supplier(TimeStampedModel, models.Model):
    name = models.CharField(_("Name"), max_length=127)
    contact_no = models.CharField(_("Contact Number"), max_length=15)
    # bank account details
    bank_name = models.CharField(_("Bank Name"), max_length=127)
    branch_name = models.CharField(_("Branch Name"), max_length=127)
    bank_acc_num = models.CharField(_("Account Number"), max_length=127)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return str(self.id)


class SupplierOrder(TimeStampedModel, models.Model):
    supplier = models.ForeignKey(Supplier, models.RESTRICT, related_name="order", verbose_name=_("Supplier"))
    item = models.ForeignKey(Item, models.RESTRICT, related_name= "supplier_order", verbose_name=_("Item"))
    ordered_quantity = models.IntegerField(_("Ordered Quantity"),)
    received_quantity = models.IntegerField(_("Received Quantity"), null=True, blank=True)
    bill_amount = models.IntegerField(_("Bill Amount"))
    paid_amount = models.IntegerField(_("Paid Amount"), null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Supplier Order")
        verbose_name_plural = _("Supplier Orders")

    def __str__(self):
        return str(self.id)
