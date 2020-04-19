import random

from django.core.management.base import BaseCommand

from todo_project._auth.models import MyUser
from todo_project.core.models import TaskList


def create_users(num):
    creators = [MyUser(username=f"User {i}") for i in range(num)]
    MyUser.objects.bulk_create(creators)


class Command(BaseCommand):
    help = 'Create data for TaskList table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of task lists for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new task list')

        parser.add_argument('-i', '--imp', action='store_true', help='Create Task list with highest importance')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')
        importance = kwargs.get('imp')

        if not prefix: prefix = 'A'

        for i in range(total):
            if importance:
                tl = TaskList.objects.create(name=f'{prefix}_task_list {i}',
                                             importance=10,
                                             creator_id=1)
            else:
                tl = TaskList.objects.create(name=f'{prefix}_book {i}',
                                             price=random.randint(0, 10),
                                             creator_id=1)
            self.stdout.write(f'Task list {tl.id} was created')

        create_users(total)
