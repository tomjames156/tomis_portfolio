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

    class Meta:
        model = Project
        fields = ['id', 'language_used', 'project_name', 'importance', 'technology_used']