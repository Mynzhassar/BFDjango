from rest_framework import serializers
from .models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name')


class TaskShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    task_list = serializers.PrimaryKeyRelatedField(required=True, queryset=TaskList.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'task_list')


class TaskFullSerializer(serializers.ModelSerializer):
    task_list_full = TaskListSerializer(read_only=True)

    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('task_list_full',)

