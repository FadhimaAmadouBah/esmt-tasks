from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Project
from .serializers import ProjectSerializer


class ProjectListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(
            created_by=user
        ) | Project.objects.filter(members=user)


class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(created_by=user) | Project.objects.filter(members=user)

    def perform_update(self, serializer):
        if self.get_object().created_by != self.request.user:
            raise PermissionDenied("Seul le créateur peut modifier ce projet.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("Seul le créateur peut supprimer ce projet.")
        instance.delete()