from django.db.models.signals import post_save
from django.dispatch import receiver

from todo_project._auth.models import MyUser, Profile


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
