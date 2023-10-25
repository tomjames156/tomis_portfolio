from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("About the Project", {"fields": ['project_name', 'about_project']})
    ]

admin.site.register(Project)
admin.site.register(TechnologyUsed)
admin.site.register(LanguageUsed)