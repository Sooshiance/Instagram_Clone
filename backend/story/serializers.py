from rest_framework.serializers import ModelSerializer

from .models import Story


class StorySerializer(ModelSerializer[Story]):
    class Meta:
        model = Story
        fields = [
            "pk",
            "user",
            "visible_for",
            "content",
            "hidden",
            "img",
            "is_visible",
            "is_archived",
            "created_at",
        ]
