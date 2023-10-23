from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200, null=False, blank=False)