from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created', 'completed']

class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
    """Minimal serializer so UpdateAPIView can validate with empty PATCH body."""
    class Meta:
        model = ToDo
        fields = ['id', 'completed']
        read_only_fields = ['id']