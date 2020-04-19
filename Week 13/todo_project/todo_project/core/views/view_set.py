from todo_project.core.models import TaskList, Task
from todo_project.core.serializers import TaskListSerializer, \
    TaskSerializer, TaskDetailedSerializer, SportsGoalsSerializer, StudyGoalsSerializer

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated

import logging
logger = logging.getLogger(__name__)


# class IsAdmin(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user and request.user.is_superuser


class TaskListsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Task list object created, ID: {serializer.instance}')
        logger.info(f'Task list object created, ID: {serializer.instance}')
        logger.warning(f'Task list object created, ID: {serializer.instance}')
        logger.error(f'Task list object created, ID: {serializer.instance}')
        logger.critical(f'Task list object created, ID: {serializer.instance}')

    # @action(methods=['GET'], detail=False)
    # def top_five(self):
    #     top_objects = TaskList.objects.all().order_by("-importance")[:5]
    #     serializer = TaskListSerializer(top_objects)
    #     return Response(serializer.data)

    # @action(methods=['PUT'], detail=True)
    # def set_rating(self, request, pk):
    #     task_list = get_object_or_404(TaskList, id=pk)
    #     task_list.set_importance(request.data.get('importance'))
    #     serializer = TaskListSerializer(task_list)
    #     return Response(serializer.data)


class TaskViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(task=self.request.task)


class StudyGoalViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = StudyGoalsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(task=self.request.task)
