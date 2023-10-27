from django.db import models
from django.contrib.auth.models import User

class UserPortfolio(models.Model):
    "An class that represents a user and their information"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500, blank=False)
    bio = models.CharField(max_length=1500, blank=False)


class SocialLink(models.Model):
    "A class the represents a social media profile link"
    user = models.ForeignKey(UserPortfolio, related_name='social_links')
    social_media = models.CharField(max_length=50, blank=False)
    link_url = models.URLField(max_length=1000, blank=False)


class Experience(models.Model):
    "A class representing previous experience/places of work"
    role = models.CharField(max_length=100, blank=False)
    timeline = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=100, blank=False)