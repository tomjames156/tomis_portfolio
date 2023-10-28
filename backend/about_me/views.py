from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

from django.contrib.auth.models import User

@api_view(['GET'])
def get_user_info(request, username):
    user = User.objects.get(username=username)
    user_info = UserPortfolio.objects.get(user=user)
    serializer = UserPortfolioSerializer(user_info)
    return Response(serializer.data)


@api_view(['GET'])
def get_experience(request, username):
    user = User.objects.get(username=username)
    users_portfolio = UserPortfolio.objects.get(user=user)
    work_experience = users_portfolio.work_experience.all()