from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "priority", "status",
            "owner", "owner_username", "due_date", "created_at", "updated_at",
        ]
        read_only_fields = ["owner", "created_at", "updated_at"]
