from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

from .serializers import *
from .models import *

from django.contrib.auth.models import User

def get_user_info(request, username):
    user = User.objects.get(username=username)
    user_info = UserPortfolio.objects.get(user=user)
    print(user_info.bio)
    return HttpResponse(user_info.bio)