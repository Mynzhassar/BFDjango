from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from todo_project.core.models import TaskList, Task
from todo_project.core.serializers import TaskListSerializer, TaskDetailedSerializer


class TaskListAPIView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListDetailAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)


class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailedSerializer
    lookup_field = "id"
