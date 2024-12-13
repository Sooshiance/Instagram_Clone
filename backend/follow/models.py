from django.db import models

from user.models import User


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following_set', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='follower_set', on_delete=models.CASCADE)
    connected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            'follower',
            'following',
        ]
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'
