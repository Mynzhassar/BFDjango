from rest_framework import serializers
from .models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskList
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'task list')
