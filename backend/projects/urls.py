from django.urls import path
from .views import *

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('projects/', get_projects, name='all_projects')
]