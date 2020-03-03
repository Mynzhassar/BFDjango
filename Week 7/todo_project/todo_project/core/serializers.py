from rest_framework import serializers
from .models import TaskList, Task, TaskType


def name_validator(name):
    for n in name:
        if not (n.isalpha() or n == " "):
            raise ValueError(f'{n} character is not permitted in NAME field')


def importance_validator(importance):
    if not (1 <= importance <= 10):
        raise ValueError(f'{importance} value is not permitted in IMPORTANCE field')


def status_validator(status):
    if status not in [0, 1, 2, 3]:
        raise ValueError(f'{status} value is not permitted in STATUS field')


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, validators=[name_validator])
    importance = serializers.IntegerField(required=False, validators=[importance_validator])

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'importance')


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    task_list = serializers.PrimaryKeyRelatedField(required=True, queryset=TaskList.objects.all())
    status = serializers.IntegerField(validators=[status_validator])

    class Meta:
        model = Task
        fields = ('id', 'name', 'status' , 'task_list')


class TaskDetailedSerializer(serializers.ModelSerializer):
    task_list_full = TaskListSerializer(read_only=True)

    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + ('task_list_full',)


class TaskTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, validators=[name_validator])
    task = serializers.IntegerField(read_only=True)

    class Meta:
        model = TaskType
        field = ('id', 'name', 'task')
