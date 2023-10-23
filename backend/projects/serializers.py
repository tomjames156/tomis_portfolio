from rest_framework.serializers import ModelSerializer
from .models import Project, TechnologyUsed, LanguageUsed
    
class TechnologySerializer(ModelSerializer):
    class Meta:
        model = TechnologyUsed
        fields = ['technology_used']


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = LanguageUsed
        fields = ['language_name']


class ProjectSerializer(ModelSerializer):
    technologies_used = TechnologySerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'