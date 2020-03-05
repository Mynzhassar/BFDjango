from todo_project.core.views.view_set import TaskListsViewSet, TaskViewSet, SportsGoalViewSet, StudyGoalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task_list', TaskListsViewSet, basename="core")
router.register(r'tasks', TaskViewSet, basename="core")
router.register(r'sport', SportsGoalViewSet, basename="core")
router.register(r'study', StudyGoalViewSet, basename="core")

urlpatterns = [

] + router.urls

