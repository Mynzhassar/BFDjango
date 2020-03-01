from django.db import models
from rest_framework import serializers

from todo_project.utils.constants import (TASK_DONE,
                                          TASK_IN_PROGRESS,
                                          TASK_NEW,
                                          TASK_TODO,
                                          TASK_STATUSES)


def valid_importance(value):
    if not (1 <= value <= 10):
        raise serializers.ValidationError("Invalid importance")


class TaskList(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now=True)
    importance = models.IntegerField(default=1,
                                     validators=[valid_importance])

    class Meta:
        verbose_name = "Task List"
        verbose_name_plural = "Task Lists"

    def __str__(self):
        return "{} task list".format(self.name)

    @property
    def started(self):
        return f'Task list has been set at {self.created_at}'

    @classmethod
    def top_important(cls):
        return TaskList.objects.all().order_by("-importance")[:10]

    @staticmethod
    def cmp(task_list1, task_list2):
        return task_list1.importance > task_list2.importance


class Task(models.Model):
    name = models.CharField(max_length=150)
    status = models.PositiveSmallIntegerField(choices=TASK_STATUSES,
                                              default=TASK_NEW)
    task_list = models.ForeignKey(TaskList,
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return "{0} in {1}".format(self.name, self.task_list)
