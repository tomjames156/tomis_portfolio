from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("About the Project", {"fields": ['project_name', 'project_description', 'project_image']}),
        ("Built With", {"fields": ['technologies_used', 'languages_used']}),
        ("Importance / Complexity", {"fields": ["importance"]})
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(TechnologyUsed)
admin.site.register(LanguageUsed)