from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from apps.quotations.models import Invoice
from apps.stakeholders.models import Client


class Task(TimeStampedModel, models.Model):
    class TaskStatuses(models.TextChoices):
        PENDING = "PENDING", _("Pending")
        ON_GOING = "ON_GOING", _("On Going")
        COMPLETED = "COMPLETED", _("Completed")
        CLOSED = "CLOSED", _("Closed")

    name = models.CharField(_("Name"), max_length=127)
    description = models.CharField(_("Description"), max_length=1023, null=True, blank=True)
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    status = models.CharField(
        _("Task Status"), max_length=50, choices=TaskStatuses.choices, default=TaskStatuses.PENDING, null=True,
        blank=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return str(self.id)


class Project(TimeStampedModel, models.Model):
    class ProjectStatuses(models.TextChoices):
        PENDING = "PENDING", _("Pending")
        APPROVED = "APPROVED", _("Approved")
        ON_GOING = "ON_GOING", _("On Going")
        COMPLETED = "COMPLETED", _("Completed")
        CLOSED = "CLOSED", _("Closed")

    name = models.CharField(_("Name"), max_length=127)
    description = models.CharField(_("Description"), max_length=1023, null=True, blank=True)
    invoice = models.ForeignKey(Invoice,on_delete=models.RESTRICT, related_name="projects", verbose_name=_("Invoice"))
    task = models.ManyToManyField(Task, blank=True)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT, related_name="projects", verbose_name=_("Client"))
    project_sum = models.DecimalField(_("Project Sum"), max_digits=15, decimal_places=2)
    profit = models.DecimalField(_("Profit"), max_digits=15, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        _("Project Status"), max_length=50, choices=ProjectStatuses.choices, default=ProjectStatuses.PENDING, null=True,
        blank=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return str(self.id)
