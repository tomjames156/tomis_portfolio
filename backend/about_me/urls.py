from django.urls import path
from .views import *

urlpatterns = [
    path('<str:username>',  get_user_info, name="get user info")
]