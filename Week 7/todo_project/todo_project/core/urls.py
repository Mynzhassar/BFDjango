from todo_project.core.views.view_set import TaskListsViewSet, TaskViewSet, TaskTypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task_list', TaskListsViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'type', TaskTypeViewSet)

urlpatterns = router.urls

