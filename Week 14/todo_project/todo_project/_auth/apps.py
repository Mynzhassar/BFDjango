from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'todo_project._auth'

    def ready(self):
        import todo_project._auth.signals
