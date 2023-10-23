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