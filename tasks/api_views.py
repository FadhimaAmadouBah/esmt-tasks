from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project__created_by=self.request.user) | \
               Task.objects.filter(assigned_to=self.request.user)


class StatisticsAPI(generics.GenericAPIView):
    def get(self, request):
        from django.utils import timezone
        from rest_framework.response import Response
        year = timezone.now().year
        tasks = Task.objects.filter(assigned_to=request.user)
        total = tasks.count()
        done = tasks.filter(status='termine').count()
        on_time = sum(1 for t in tasks if t.completed_on_time())
        rate = round((on_time / total * 100)) if total > 0 else 0
        prime = 100000 if rate == 100 else (30000 if rate >= 90 else 0)
        return Response({
            'year': year, 'total_tasks': total,
            'done_tasks': done, 'on_time': on_time,
            'completion_rate': rate, 'prime': prime
        })