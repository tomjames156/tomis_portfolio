from django.urls import path
from .views import *

urlpatterns = [
    path('', initial, name='about_api'),
    path('<str:username>/projects/', get_projects, name='all_projects'),
    path('<str:username>/technologies/', get_technologies, name='my_tech_stack'),
    path('technology_used/<str:technology_used>', get_projects_by_technology, name='project_built_with_technology'),
    path('language_used/<str:language_name>', get_projects_by_language, name='project_built_with_language'),
    path('language_technologies/<str:language_name>', get_technologies_built_with, name='technologies_built_with_language')
]