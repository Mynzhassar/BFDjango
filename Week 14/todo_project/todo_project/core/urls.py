from django.urls import path

from todo_project.core.views.view_set import TaskListsViewSet, SportTaskViewSet, StudyTaskViewSet
from todo_project.core.views.views import TaskListDetailAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task_list', TaskListsViewSet, basename="core")
router.register(r'sport', SportTaskViewSet, basename="core")
router.register(r'study', StudyTaskViewSet, basename="core")

urlpatterns = [
    path('task_list/<int:id>/', TaskListDetailAPIView.as_view()),
] + router.urls
