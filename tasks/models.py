from django.db import models
from django.utils import timezone
from users.models import CustomUser
from projects.models import Project


class Task(models.Model):
    STATUS_CHOICES = [
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    ]
    PRIORITY_CHOICES = [
        ('basse', 'Basse'),
        ('normale', 'Normale'),
        ('haute', 'Haute'),
        ('urgente', 'Urgente'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='a_faire')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normale')
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == 'termine' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'termine':
            self.completed_at = None
        super().save(*args, **kwargs)

    def is_overdue(self):
        if self.due_date and self.status != 'termine':
            return timezone.now() > self.due_date
        return False

    def completed_on_time(self):
        if self.completed_at and self.due_date:
            return self.completed_at <= self.due_date
        return False


class PrimeEvaluation(models.Model):
    PERIOD_CHOICES = [
        ('T1', 'Trimestre 1'),
        ('T2', 'Trimestre 2'),
        ('T3', 'Trimestre 3'),
        ('T4', 'Trimestre 4'),
        ('annuel', 'Annuel'),
    ]

    professeur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='evaluations')
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    year = models.IntegerField()
    total_tasks = models.IntegerField(default=0)
    tasks_on_time = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0)
    prime_amount = models.IntegerField(default=0)

    def calculate_prime(self):
        if self.total_tasks == 0:
            return 0
        self.completion_rate = (self.tasks_on_time / self.total_tasks) * 100
        if self.completion_rate == 100:
            self.prime_amount = 100000
        elif self.completion_rate >= 90:
            self.prime_amount = 30000
        else:
            self.prime_amount = 0
        return self.prime_amount