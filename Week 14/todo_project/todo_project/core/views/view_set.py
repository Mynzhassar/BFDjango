from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from todo_project.core.models import TaskList, SportGoal, StudyGoal
from todo_project.core.serializers import TaskListSerializer, SportsGoalSerializer, SportsGoalDetailedSerializer, \
    StudyGoalSerializer, StudyGoalDetailedSerializer

from rest_framework import viewsets, request
from rest_framework import mixins
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

import logging

logger = logging.getLogger(__name__)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


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

    def get_queryset(self):
        queryset = self.queryset.filter(creator=self.request.user)
        return queryset

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


class SportTaskViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = SportGoal.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SportsGoalSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return SportsGoalSerializer
    #     if self.action == 'retrieve':
    #         return SportsGoalDetailedSerializer

    #     return SportsGoalSerializer


class StudyTaskViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = StudyGoal.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StudyGoalDetailedSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return StudyGoalSerializer
    #     if self.action == 'retrieve':
    #         return StudyGoalDetailedSerializer
    #
    #     return StudyGoalSerializer
