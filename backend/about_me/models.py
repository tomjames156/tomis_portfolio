from django.db import models
from django.contrib.auth.models import User

class UserPortfolio(models.Model):
    "An class that represents a user and their information"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500, blank=False)
    bio = models.CharField(max_length=1500, blank=False)

    def __str__(self):
        return self.user.username


class SocialLink(models.Model):
    "A class the represents a social media profile link"
    user = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE, related_name='social_media')
    social_media = models.CharField(max_length=50, blank=False)
    link_url = models.URLField(max_length=1000, blank=False)

    def __str__(self):
        return f"{self.user} - {self.social_media}"


class Experience(models.Model):
    "A class representing previous experience/places of work"
    user = models.ForeignKey(UserPortfolio, on_delete=models.CASCADE, related_name='work_experience')
    role = models.CharField(max_length=100, blank=False)
    timeline = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.user} - {self.company}"

    class Meta:
        verbose_name_plural = 'Work Experiences'


class BulletPoint(models.Model):
    "A class representing a bullet point an experience class"
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bullet_points')
    bullet_text = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.bullet_text[:30]