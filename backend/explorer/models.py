import uuid

from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)

from post.models import Post


class Explorer(models.Model):
    eid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, max_length=50
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # TODO:
    all_data = models.FloatField(
        validators=[MinValueValidator(1.00), MaxValueValidator(100.00)]
    )
    first_day_data = models.FloatField(
        validators=[MinValueValidator(1.00), MaxValueValidator(100.00)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["all_data"]
        indexes = [models.Index(fields=("eid",))]
        verbose_name = "Explorer"
        verbose_name_plural = "Explorer"
