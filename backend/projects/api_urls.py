from django.urls import path
from . import api_views

urlpatterns = [
    path('projects/', api_views.ProjectListCreateAPI.as_view(), name='api_project_list'),
    path('projects/<int:pk>/', api_views.ProjectDetailAPI.as_view(), name='api_project_detail'),
]