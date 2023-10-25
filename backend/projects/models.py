from django.db import models

# Create your models here.

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
    project_name = models.CharField(max_length=200, null=False, blank=False)
    project_description = models.CharField(max_length=5000, null=True, blank=True)
    project_image = models.ImageField(upload_to='project_images', null=True)
    technology_used = models.ForeignKey(TechnologyUsed, on_delete=models.CASCADE, null=True)
    language_used = models.ForeignKey(LanguageUsed, on_delete=models.CASCADE, null=True)
    levels = [
        ('1', 'complex'),
        ('2', 'proud of'),
        ('3', 'easy')
    ]
    importance = models.CharField(choices=levels, max_length=1, default='1')

    def __str__(self):
        return self.project_name