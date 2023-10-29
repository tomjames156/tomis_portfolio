from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User

from .models import *
from .serializers import *


@api_view(['GET'])
def initial(request):
    "Describes the api endpoints, access methods and return values"
    routes = [
        {
            "Endpoint": 'username/projects/',
            'method': 'GET',
            'body': None,
            'description': "Returns a list of an existing user's projects based on the username provided"
        }
    ]
    return Response(routes)


@api_view(['GET'])
def get_projects(request, username):
    "Returns a list of the users projects based on the username provided"
    try:
        user = User.objects.get(username=username)
        projects = user.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    except (User.DoesNotExist, ValueError):
        content = {"User Not Found": f"The user '{username}' does not exist"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_technologies(request, username):
    try:
        user = User.objects.get(username=username)
        technologies = user.technologies_used.all
        serializer = TechnologySerializer(technologies, many=True)
        return Response(serializer.data)
    except (User.DoesNotExist, ValueError):
        content = {"User Not Found": f"The user '{username}' does not exist"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


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
