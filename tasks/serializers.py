from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to',
                  'created_by', 'status', 'priority', 'due_date', 'completed_at',
                  'created_at', 'is_overdue']
        read_only_fields = ['created_by', 'completed_at', 'created_at']

    def get_is_overdue(self, obj):
        return obj.is_overdue()