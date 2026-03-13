from rest_framework import serializers
from .models import Task, PrimeEvaluation
from users.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to', 'assigned_to_detail',
                  'created_by', 'status', 'priority', 'due_date', 'completed_at',
                  'is_overdue', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'completed_at', 'created_at', 'updated_at']

    def get_is_overdue(self, obj):
        return obj.is_overdue()

    def validate(self, data):
        request = self.context.get('request')
        if request and request.user.is_etudiant:
            assigned = data.get('assigned_to')
            if assigned and assigned.is_professeur:
                raise serializers.ValidationError(
                    "Les étudiants ne peuvent pas assigner une tâche à un professeur."
                )
        return data


class PrimeEvaluationSerializer(serializers.ModelSerializer):
    professeur = UserSerializer(read_only=True)

    class Meta:
        model = PrimeEvaluation
        fields = '__all__'