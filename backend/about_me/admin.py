from django.contrib import admin
from .models import *


class SocialMediaInline(admin.StackedInline):
    model = SocialLink
    extra = 3
    verbose_name_plural = 'Social Media'
    verbose_name = 'Social Media Link'


class UserPortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Info", {"fields": ['user', 'email', 'bio']})
    ]
    inlines = [SocialMediaInline]

admin.site.register(UserPortfolio, UserPortfolioAdmin)


class BulletPointInline(admin.StackedInline):
    model = BulletPoint
    extra = 3 


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    verbose_name_plural = 'Work Experience'

    fieldsets = [
        ("Role & Company", {'fields': ["user", "role", "company", "timeline"]})
    ]
    
    inlines = [BulletPointInline]
    
admin.site.register(Experience, ExperienceAdmin)