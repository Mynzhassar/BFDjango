from django.contrib import admin

from todo_project.core.models import TaskList, Task, SportsGoal, StudyGoals


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'importance')
    search_fields = ('name',)
    ordering = ('importance',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_list')


@admin.register(SportsGoal)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task')


@admin.register(StudyGoals)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task')
