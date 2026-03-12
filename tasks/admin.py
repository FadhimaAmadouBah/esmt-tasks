from django.contrib import admin
from .models import Task, PrimeEvaluation


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'assigned_to', 'status', 'priority', 'due_date']
    list_filter = ['status', 'priority']


@admin.register(PrimeEvaluation)
class PrimeEvaluationAdmin(admin.ModelAdmin):
    list_display = ['professeur', 'period', 'year', 'completion_rate', 'prime_amount']