from django.contrib import admin

from apps.employees.models import Employee, Attendance, Salary
from config.admin import custom_admin_site


@admin.register(Employee, site=custom_admin_site)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendance, site=custom_admin_site)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Salary, site=custom_admin_site)
class SalaryAdmin(admin.ModelAdmin):
    pass


