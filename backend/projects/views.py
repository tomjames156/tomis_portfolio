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
