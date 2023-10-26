from django.contrib import admin
from .models import *

class ScreenShotInline(admin.StackedInline):
    model = ScreenShot
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Overview", {"fields": ['project_name', 'project_description', 'project_image', "complexity"]}),
        ("Built With", {"fields": ['technologies_used', 'languages_used']}),
        ("View Project", {"fields": ['hosted', 'repository_link', 'live_site']})
    ]
    inlines = [ScreenShotInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(TechnologyUsed)
admin.site.register(LanguageUsed)