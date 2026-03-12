from django.urls import path
from .api_views import ProjectListCreateAPI, ProjectDetailAPI, TaskListCreateAPI

urlpatterns = [
    path('projects/', ProjectListCreateAPI.as_view(), name='api_projects'),
    path('projects/<int:pk>/', ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('projects/<int:pk>/tasks/', TaskListCreateAPI.as_view(), name='api_project_tasks'),
]