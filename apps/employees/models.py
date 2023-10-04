from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Employee(TimeStampedModel, models.Model):
    name = models.CharField(_("Name"), max_length=127)
    reg_no = models.CharField(_("Registered Number"), max_length=15)
    contact_no = models.CharField(_("Contact Number"), max_length=15)
    address = models.CharField(_("Address"), max_length=1023)

    # bank account details
    bank_name = models.CharField(_("Bank Name"), max_length=127)
    branch_name = models.CharField(_("Branch Name"), max_length=127)
    bank_acc_num = models.CharField(_("Account Number"), max_length=127)

    salary_amount = models.DecimalField(_("Salary Amount"), max_digits=15, decimal_places=2)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self):
        return str(self.name)


class Attendance(TimeStampedModel, models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE, related_name="employee", verbose_name=_("Attendance"))
    date = models.DateField(_("Date"))
    ot_hours = models.DecimalField(_("OT Hours"), max_digits=7, decimal_places=2)
    is_leave = models.BooleanField(_("Is Leave"),default=False)
    leave_type = models.CharField(_("Leave Type"), max_length=127, null=True, blank=True)
    notes = models.CharField(_("Notes"), max_length=1023, null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Attendance")
        verbose_name_plural = _("Attendances")

    def __str__(self):
        return str(self.id)


class Salary(TimeStampedModel, models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE, related_name="salary", verbose_name=_("Employee"))
    amount = models.DecimalField(_("Amount"),  max_digits=15, decimal_places=2)
    is_advance = models.BooleanField(_("Is Advance"), default=False)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Salary")
        verbose_name_plural = _("Salaries")

    def __str__(self):
        return str(self.id)

