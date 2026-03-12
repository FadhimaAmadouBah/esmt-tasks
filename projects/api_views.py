from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from tasks.serializers import TaskSerializer
from tasks.models import Task


class ProjectListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user) | \
               Project.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)


class TaskListCreateAPI(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['pk'])
        serializer.save(project=project, created_by=self.request.user)