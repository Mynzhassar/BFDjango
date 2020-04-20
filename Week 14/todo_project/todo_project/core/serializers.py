from rest_framework import serializers
from .models import TaskList, SportGoal, StudyGoal
from .._auth.models import MyUser
from todo_project._auth.serializers import UserSerializer


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
    creator_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(required=True, validators=[name_validator])
    importance = serializers.IntegerField(required=False, validators=[importance_validator])

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'photo', 'importance', 'creator_id')


class StudyGoalSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[name_validator])
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = StudyGoal
        fields = ('id', 'name', 'user')


class SportsGoalSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[name_validator])
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SportGoal
        fields = ('id', 'name', 'user', 'task_list_id')


class SportsGoalDetailedSerializer(serializers.ModelSerializer):

    class Meta(SportsGoalSerializer.Meta):
        fields = SportsGoalSerializer.Meta.fields + ('task_list', )


class StudyGoalDetailedSerializer(serializers.ModelSerializer):

    class Meta(StudyGoalSerializer.Meta):
        fields = StudyGoalSerializer.Meta.fields + ('task_list', )
