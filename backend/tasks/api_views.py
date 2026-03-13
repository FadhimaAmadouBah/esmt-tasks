from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Task, PrimeEvaluation
from .serializers import TaskSerializer, PrimeEvaluationSerializer
from projects.models import Project
from users.models import CustomUser
from django.utils import timezone


class TaskListCreateAPI(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Task.objects.filter(project__id=project_id)
        return Task.objects.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(pk=project_id)
        if project.created_by != self.request.user:
            raise PermissionDenied("Seul le créateur peut ajouter des tâches.")
        serializer.save(created_by=self.request.user, project=project)


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_update(self, serializer):
        task = self.get_object()
        user = self.request.user
        is_creator = task.project.created_by == user
        is_assigned = task.assigned_to == user

        if not is_creator and not is_assigned:
            raise PermissionDenied("Permission refusée.")

        if not is_creator and is_assigned:
            # L'assigné ne peut changer que le statut
            allowed = {'status'}
            if set(serializer.validated_data.keys()) - allowed:
                raise PermissionDenied("Vous ne pouvez changer que le statut.")

        serializer.save()


class StatisticsAPI(APIView):
    def get(self, request):
        year = int(request.query_params.get('year', timezone.now().year))
        period = request.query_params.get('period', 'annuel')

        if request.user.is_staff or request.user.is_professeur:
            professeurs = CustomUser.objects.filter(role='professeur')
            evaluations = []
            for prof in professeurs:
                tasks = prof.assigned_tasks.filter(due_date__year=year)
                total = tasks.count()
                on_time = sum(1 for t in tasks.filter(status='termine') if t.completed_on_time())
                rate = round((on_time / total * 100), 1) if total > 0 else 0
                prime = 100000 if rate == 100 else (30000 if rate >= 90 else 0)
                evaluations.append({
                    'id': prof.id,
                    'name': prof.get_full_name() or prof.username,
                    'total_tasks': total,
                    'on_time': on_time,
                    'completion_rate': rate,
                    'prime': prime
                })
            return Response({'evaluations': evaluations, 'year': year})
        return Response({'error': 'Permission refusée'}, status=403)