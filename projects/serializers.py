from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    completion_rate = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_by', 'members', 'completion_rate', 'created_at']

    def get_completion_rate(self, obj):
        return obj.get_completion_rate()