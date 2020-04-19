from django.db import models
from todo_project.utils.validators import validate_file_size, validate_extension
from todo_project._auth.models import MyUser

from todo_project.utils.constants import (TASK_STATUSES,
                                          TASK_NEW,
                                          TASK_TODO,
                                          TASK_IN_PROGRESS,
                                          TASK_DONE)


# Base models of the project

class TaskList(models.Model):
    photo = models.ImageField(upload_to='media/photos',
                              validators=[validate_file_size,
                                          validate_extension],
                              null=True, blank=True)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    importance = models.IntegerField(default=0)

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
    def compare(task_list1, task_list2):
        return task_list1.importance > task_list2.importance


class TaskType(models.Model):
    status = models.PositiveSmallIntegerField(choices=TASK_STATUSES, default=TASK_NEW)
    name = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, default="")
    is_finished = models.BooleanField(default=False)

    class Meta:
        abstract = True


class StudyGoal(TaskType):
    pass

    class Meta:
        verbose_name = "Goal at the university"
        verbose_name_plural = "Goals at the university"

    def __str__(self):
        return f'{self.name} in university'


class SportGoal(TaskType):
    pass

    class Meta:
        verbose_name = "Goal at sports"
        verbose_name_plural = "Goals at sports"

    def __str__(self):
        return f'{self.name} at sports'


# Models of managers

class TaskNewManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_NEW)

    def filter_by_status(self, status):
        return self.filter(status=status)


class TaskToDoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_TODO)

    def filter_by_status(self, status):
        return self.filter(status=status)


class TaskProgressManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_IN_PROGRESS)

    def filter_by_status(self, status):
        return self.filter(status=status)


class TaskDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)
