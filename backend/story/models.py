from typing import (
    TYPE_CHECKING
)

from django.db import models

from user.models import User

if TYPE_CHECKING:
    from user.models import User as UserType


class Story(models.Model):
    user: UserType = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stories"
    )
    visible_for = models.DurationField(default=86400)
    content = models.CharField(max_length=512, blank=True, null=True)
    hidden = models.BooleanField(default=False)
    likes = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    img = models.ImageField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"


class Reaction(models.Model):
    user: UserType = models.ForeignKey(User, on_delete=models.CASCADE)
    story: UserType = models.ForeignKey(Story, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "story")
        verbose_name = "Story"
        verbose_name_plural = "Stories"
