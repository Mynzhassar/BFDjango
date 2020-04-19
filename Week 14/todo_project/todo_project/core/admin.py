from django.contrib import admin

from todo_project.core.models import TaskList, SportGoal, StudyGoal


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'importance')
    search_fields = ('name',)
    ordering = ('importance',)


@admin.register(SportGoal)
class SportTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_list')


@admin.register(StudyGoal)
class StudyTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_list')
