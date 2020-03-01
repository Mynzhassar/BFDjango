from django.contrib import admin

from todo_project.core.models import TaskList, Task


@admin.register(TaskList)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'importance')
    ordering = ('importance',)


@admin.register(Task)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')