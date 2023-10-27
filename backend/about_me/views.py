from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from .models import *

def get_user_info(request, username):
    user_info = UserPortfolio.objects.get(username=username)
    serializer = UserPortfolioSerializer(user_info)
    return Response(serializer.data)