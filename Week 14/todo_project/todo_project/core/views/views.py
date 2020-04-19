from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from todo_project.core.models import TaskList
from todo_project.core.serializers import TaskListSerializer


class TaskListDetailAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
