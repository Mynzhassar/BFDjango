from django.core.management.base import BaseCommand
from todo_project.core.models import TaskList


class Command(BaseCommand):
    help = 'Delete data for TaskList table'

    def add_arguments(self, parser):
        parser.add_argument('task_list_ids', nargs='+', help='Task list ids for delete')

    def handle(self, *args, **kwargs):

        for tl_id in kwargs['task_list_ids']:
            try:
                tl = TaskList.objects.get(id=tl_id)
                tl.delete()
                self.stdout.write(self.style.SUCCESS(f"Task list id: {tl_id} was deleted successfully"))
            except TaskList.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f"Task list id: {tl_id} does not exists!"))