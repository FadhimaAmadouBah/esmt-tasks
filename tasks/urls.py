from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('statistics/', views.statistics_view, name='statistics'),
]