from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=False, blank=False)
    about_project = models.CharField(max_length=5000, null=True, blank=True) # to-do change the blankness 

    def __str__(self):
        return self.project_name
    

class TechnologyUsed(models.Model):
    technology_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.technology_name
    


class LanguageUsed(models.Model):
    language_name = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.language_name