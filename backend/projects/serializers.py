from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, source='members',
        queryset=__import__('users.models', fromlist=['CustomUser']).CustomUser.objects.all()
    )
    completion_rate = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_by', 'members', 'member_ids',
                  'completion_rate', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def get_completion_rate(self, obj):
        return obj.get_completion_rate()

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)