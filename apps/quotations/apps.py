from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuotationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.quotations"
    verbose_name = _("Quotation")
    verbose_name_plural = _("Quotations")
