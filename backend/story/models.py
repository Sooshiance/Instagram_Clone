from django.db import models

from user.models import User


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    visible_for = models.DurationField(default=86400)
    content = models.CharField(max_length=512, blank=True, null=True)
    hidden = models.BooleanField(default=False)
    likes = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    img = models.ImageField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'story')
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
