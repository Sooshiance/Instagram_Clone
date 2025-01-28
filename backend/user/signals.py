from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from .models import Profile, User


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
            is_private=user.is_private,
        )


@receiver(pre_save, sender=Profile)
def update_user(sender, instance, **kwargs):
    if instance.pk:
        user = instance.user
        user.username = instance.username
        user.is_private = instance.is_private
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)


post_delete.connect(delete_user, sender=Profile)
