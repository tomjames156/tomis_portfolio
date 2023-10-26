from django.contrib import admin
from .models import *

class ScreenShotInline(admin.StackedInline):
    model = ScreenShot
    extra = 3


class RepositoryInline(admin.StackedInline):
    model = Repository
    extra = 2


class LiveSiteInline(admin.StackedInline):
    model = LiveSite
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Overview", {"fields": ['project_name', 'project_description', 'project_image', "complexity"]}),
        ("Built With", {"fields": ['technologies_used', 'languages_used']}),
        ("View Project", {"fields": ['hosted', 'hostable']})
    ]
    inlines = [ScreenShotInline, RepositoryInline, LiveSiteInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(TechnologyUsed)
admin.site.register(LanguageUsed)