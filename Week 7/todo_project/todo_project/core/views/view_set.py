from todo_project.core.models import TaskList, Task, TaskType
from todo_project.core.serializers import TaskListSerializer, \
    TaskSerializer, TaskDetailedSerializer, SportsGoalsSerializer, StudyGoalsSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request in SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser


class TaskListsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAdminOrReadOnly,)

    @action(methods=['GET'], detail=False)
    def top_five(self):
        top_objects = TaskList.objects.all().order_by("-importance")[:5]
        serializer = TaskListSerializer(top_objects)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=True)
    def set_rating(self, request, pk):
        task_list = get_object_or_404(TaskList, id=pk)
        task_list.set_importance(request.data.get('importance'))
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data)


class TaskViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    # permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskSerializer
        if self.action == 'retrieve':
            return TaskDetailedSerializer

        return TaskSerializer


class SportsGoalViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = SportsGoalsSerializer

    def get_queryset(self):
        return Task.objects.filter(task=self.request.task)


class StudyGoalViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = StudyGoalsSerializer

    def get_queryset(self):
        return Task.objects.filter(task=self.request.task)
