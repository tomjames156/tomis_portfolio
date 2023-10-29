from django.db import models
from django.contrib.auth.models import User


class LanguageUsed(models.Model):
    language_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.language_name
    
    class Meta:
        verbose_name_plural = 'Languages Used'



class TechnologyUsed(models.Model):
    technology_name = models.CharField(max_length=100, blank=False, null=False)
    language_used = models.ForeignKey(LanguageUsed, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.technology_name
    
    class Meta:
        verbose_name_plural = 'Technologies Used'


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=200, null=False, blank=False)
    project_description = models.CharField(max_length=5000, null=True, blank=True)
    project_image = models.ImageField(upload_to='project_images', default='project_images/no_image.png', null=True, blank=True)
    technologies_used = models.ManyToManyField(TechnologyUsed, related_name='projects', blank=True)
    languages_used = models.ManyToManyField(LanguageUsed, related_name='projects')
    levels = [
        ('1', 'complex'),
        ('2', 'challenging'),
        ('3', 'intermediate'),
        ('4', 'beginner')
    ]
    complexity = models.CharField(choices=levels, max_length=1, default='1')
    hosted = models.BooleanField(default=False)
    hostable = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
    

class ScreenShot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="screenshots")
    screenshot = models.ImageField(upload_to='project_images/screenshots', null=False)

    def __str__(self):
        return f"{self.project.project_name} - screenshot {self.pk}"
    
    class Meta:
        verbose_name_plural = 'Screenshots'
    

class Repository(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='repositories')
    repository_name = models.CharField(max_length=300, blank=False)
    repository_link = models.URLField(max_length=1000, blank=False)


class LiveSite(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='live_site')
    site_name = models.CharField(max_length=300, blank=False)
    site_url = models.URLField(max_length=1000, blank=False)