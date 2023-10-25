from rest_framework import serializers
from .models import Project, TechnologyUsed, LanguageUsed


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageUsed
        fields = ['language_name']


class TechnologySerializer(serializers.ModelSerializer):
    language_used = LanguageSerializer()

    class Meta:
        model = TechnologyUsed
        fields = ['technology_name', 'language_used']


class ProjectSerializer(serializers.ModelSerializer):
    importance = serializers.IntegerField()
    languages_used = serializers.StringRelatedField(many=True)
    technologies_used = TechnologySerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'importance', 'languages_used', 'technologies_used']