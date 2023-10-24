from django.urls import path
from .views import *

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('projects/', get_projects, name='all_projects'),
    path('technologies/', get_technologies, name='my_tech_stack'),
    path('technology_used/<str:technology_used>', get_project_by_technology, name='project_built_with_technology'),
    path('language_used/<str:language_name>', get_project_by_language, name='project_built_with_language')
]