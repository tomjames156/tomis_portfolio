from django.db import models

# Create your models here.

class LanguageUsed(models.Model):
    language_name = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.language_name

class TechnologyUsed(models.Model):
    technology_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.technology_name

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=False, blank=False)
    about_project = models.CharField(max_length=5000, null=True, blank=True) # to-do change the blankness
    technology_used = models.ManyToManyField(TechnologyUsed)
    language_used = models.ManyToManyField(LanguageUsed)
    levels = [
        (1, 'complex'),
        (2, 'proud of'),
        (3, 'easy')
    ]
    importance = models.CharField(choices=levels, max_length=1)

    def __str__(self):
        return self.project_name