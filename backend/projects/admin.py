from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("About the Project", {"fields": ['project_name', 'project_description', 'project_image']}),
        ("Built With", {"fields": ['technology_used', 'language_used']}),
        ("Importance / Complexity", {"fields": ["importance"]})
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(TechnologyUsed)
admin.site.register(LanguageUsed)