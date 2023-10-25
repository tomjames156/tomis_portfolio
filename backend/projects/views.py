from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

def welcome(request):
    return HttpResponse('Hello World')


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
def get_project_by_technology(request, technology_used):
    try:
        technology = TechnologyUsed.objects.get(technology_name=technology_used)
        projects = Project.objects.filter(technology_used=technology)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    except (TechnologyUsed.DoesNotExist, ValueError):
        return Response(f"I haven't built anything with {technology_used}")
    

@api_view(['GET'])
def get_project_by_language(request, language_name):
    try:
        language = LanguageUsed.objects.get(language_name=language_name)
        built_with_language = TechnologyUsed.objects.filter(language_used=language)
        print(built_with_language)
        # if list(built_with_language) != []:
        #     tech_stack
        # technology_used=TechnologyUsed.objects.get()
        projects_language = Project.objects.filter(language_used=language)
        serializer = ProjectSerializer(projects_language, many=True)
        return Response(serializer.data)
    except (LanguageUsed.DoesNotExist, ValueError):
        return Response(f"I haven't built anything with {language_name}")
    

@api_view(['GET'])
def get_technologies_language_built(request, language_name):
    try:
        language = LanguageUsed.objects.get(language_name=language_name)
        technolgies = TechnologyUsed.objects.filter(language_used=language )
        serializer = TechnologySerializer(technolgies, many=True)
        return Response(serializer.data)
    except (LanguageUsed.DoesNotExist, TechnologyUsed.DoesNotExist, ValueError):
        return Response(f'No {language_name} frameworks in my tech stack')
