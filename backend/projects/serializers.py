from rest_framework import serializers
from .models import Project, TechnologyUsed, LanguageUsed, ScreenShot


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageUsed
        fields = ['language_name']


class TechnologySerializer(serializers.ModelSerializer):
    language_used = LanguageSerializer()

    class Meta:
        model = TechnologyUsed
        fields = ['technology_name', 'language_used']


class ScreenShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenShot
        fields = ['screenshot']


class ProjectSerializer(serializers.ModelSerializer):
    complexity = serializers.IntegerField()
    languages_used = serializers.StringRelatedField(many=True)
    technologies_used = TechnologySerializer(many=True)
    screenshots = ScreenShotSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'project_description', 'project_image', 'complexity', 'languages_used', 'technologies_used', 'screenshots']