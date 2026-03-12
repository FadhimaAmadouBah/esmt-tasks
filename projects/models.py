from django.db import models
from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_projects')
    members = models.ManyToManyField(CustomUser, related_name='member_projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_completion_rate(self):
        total = self.tasks.count()
        if total == 0:
            return 0
        done = self.tasks.filter(status='termine').count()
        return round((done / total) * 100)