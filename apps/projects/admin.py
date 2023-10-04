from django.contrib import admin

from apps.projects.models import Task, Project
from config.admin import custom_admin_site


@admin.register(Task, site=custom_admin_site)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Project, site=custom_admin_site)
class ProjectAdmin(admin.ModelAdmin):
    pass


