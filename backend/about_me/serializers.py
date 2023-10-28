from rest_framework import serializers
from .models import *

class SocialMediaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['social_media', 'link_url']

class UserPortfolioSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerilizer(many=True)

    class Meta:
        model = UserPortfolio
        fields = ['user', 'email', 'bio']


class BulletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletPoint
        fields = ['bullet_text']


class ExperienceSerializer(serializers.ModelSerializer):
    bullet_points = BulletsSerializer(many=True)

    class Meta:
        model = Experience
        fields = ['role', 'timeline', 'company', 'bullet_points']