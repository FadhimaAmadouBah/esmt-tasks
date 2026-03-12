from django.urls import path
from .api_views import TaskDetailAPI, StatisticsAPI

urlpatterns = [
    path('tasks/<int:pk>/', TaskDetailAPI.as_view(), name='api_task_detail'),
    path('statistics/', StatisticsAPI.as_view(), name='api_statistics'),
]