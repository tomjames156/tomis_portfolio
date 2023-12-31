from django.urls import path
from .views import *

urlpatterns = [
    path('', initial, name='api_info'),
    path('<str:username>/',  get_user_info, name="get user info"),
    path('<str:username>/work_experience', get_experience, name="get user work experience")
]