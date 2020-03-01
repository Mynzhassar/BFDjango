from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="")
    importance = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Task List"
        verbose_name_plural = "Task Lists"

    def __str__(self):
        return "{} task list".format(self.name)


class Task(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    task_list = models.ForeignKey(TaskList,
                                  on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return "{0} in {1}".format(self.name, self.task_list)
