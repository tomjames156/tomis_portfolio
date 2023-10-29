from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

from django.contrib.auth.models import User


@api_view(['GET'])
def initial(request):
    "Describes the api endpoints, access methods and return values"
    routes = [
        {
            'Endpoint': 'about/username/',
            'method': 'GET',
            'body': None,
            'description': "Returns an existing user's basic information like the email, bio, and social media accounts."
        },
        {
            'Endpoint': 'about/username/work_experience/',
            'method': 'GET',
            'body': None,
            'description': "Returns a list an existing user's work experience"
        }
    ]

    return Response(routes)


@api_view(['GET'])
def get_user_info(request, username):
    "Gets a user's info based on username provided"
    user = User.objects.get(username=username)
    user_info = UserPortfolio.objects.get(user=user)
    serializer = UserPortfolioSerializer(user_info)
    return Response(serializer.data)


@api_view(['GET'])
def get_experience(request, username):
    "Gets a user's work experience based on username provided"
    user = User.objects.get(username=username)
    users_portfolio = UserPortfolio.objects.get(user=user)
    work_experience = users_portfolio.work_experience.all()
    serializer = ExperienceSerializer(work_experience, many=True)
    return Response(serializer.data)