from django.urls import path
from . import api_views

urlpatterns = [
    path('projects/<int:project_pk>/tasks/', api_views.TaskListCreateAPI.as_view(), name='api_task_list'),
    path('tasks/<int:pk>/', api_views.TaskDetailAPI.as_view(), name='api_task_detail'),
    path('tasks/my/', api_views.TaskListCreateAPI.as_view(), name='api_my_tasks'),
    path('statistics/', api_views.StatisticsAPI.as_view(), name='api_statistics'),
]