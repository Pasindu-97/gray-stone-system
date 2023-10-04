from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Item(TimeStampedModel, models.Model):
    name = models.CharField(_("Name"), max_length=127)
    description = models.CharField(_("Description"), max_length=1023, null=True, blank=True)
    unit = models.CharField(_("Unit"), max_length=15)
    unit_rate = models.DecimalField(_("Unit Rate"), max_digits=15, decimal_places=2)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return str(self.name)


class Quotation(TimeStampedModel, models.Model):
    name = models.CharField(_("Name"), max_length=127)
    description = models.CharField(_("Description"), max_length=1023, null=True, blank=True)
    total = models.DecimalField(_("Total"), max_digits=15, decimal_places=2)
    status = models.CharField(_("Status"), max_length=1023, null=True, blank=True)  #Todo: what are the statuses

    class Meta:
        ordering = ["id"]
        verbose_name = _("Quotation")
        verbose_name_plural = _("Quotations")

    def __str__(self):
        return str(self.id)


class QuotationItem(TimeStampedModel, models.Model):
    quotation = models.ForeignKey(Quotation, models.RESTRICT, related_name="items", verbose_name=_("Quotation"))
    item = models.ForeignKey(Item, models.RESTRICT, related_name="quotation_item", verbose_name=_("Item"))
    quantity = models.DecimalField(_("Quantity"), max_digits=15, decimal_places=2)

    class Meta:
        ordering = ["id"]
        verbose_name = _("QuotationItem")
        verbose_name_plural = _("QuotationItems")

    def __str__(self):
        return str(self.id)


class Invoice(TimeStampedModel, models.Model):
    quotation = models.ForeignKey(Quotation, models.CASCADE, related_name="invoice", verbose_name=_("Quotation"))
    status = models.CharField(_("Status"), max_length=1023, null=True, blank=True)  # Todo: what are the statuses

    class Meta:
        ordering = ["id"]
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self):
        return str(self.id)

