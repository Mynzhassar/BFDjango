from django.urls import path
from .views import TaskListAPIView


urlpatterns = [
    path("tasklists", TaskListAPIView.as_view()),
    #path("tasklists/")
]