from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

def welcome(request):
    return HttpResponse("Welcome to Tomi's portfolio API. Learn about the projects in my portfolio😊")


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_technologies(request):
    technologies = TechnologyUsed.objects.all()
    serializer = TechnologySerializer(technologies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_projects_by_technology(request, technology_used):
    try:
        technology = TechnologyUsed.objects.get(technology_name=technology_used)
        projects = technology.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    except (TechnologyUsed.DoesNotExist, ValueError):
        content = {'No projects found': f"I haven't built anything with {technology_used}"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_projects_by_language(request, language_name):
    try:
        language = LanguageUsed.objects.get(language_name=language_name)
        projects = language.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    except (LanguageUsed.DoesNotExist, ValueError):
        content = {'No projects found': f"I haven't built anything with {language_name}"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_technologies_built_with(request, language_name):
    try:
        language = LanguageUsed.objects.get(language_name=language_name)
        technolgies = TechnologyUsed.objects.filter(language_used=language )
        serializer = TechnologySerializer(technolgies, many=True)
        return Response(serializer.data)
    except (LanguageUsed.DoesNotExist, TechnologyUsed.DoesNotExist, ValueError):
        content = {'Framework not found': f"No {language_name} frameworks in my tech stack"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
