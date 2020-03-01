from django.urls import path
from todo_project.core.views import TaskListAPIView, TaskListDetailAPIView, TaskAPIView
from todo_project.core.views.view_set import TaskListsViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("task_lists/", TaskListAPIView.as_view()),
    path("task_lists/<int:id>/", TaskListDetailAPIView.as_view()),
    path("task_lists/<int:id>/tasks/", TaskAPIView.as_view())
]

