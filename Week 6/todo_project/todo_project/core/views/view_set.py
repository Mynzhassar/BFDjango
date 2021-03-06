from todo_project.core.models import TaskList
from todo_project.core.serializers import TaskListSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action


class TaskListsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

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
