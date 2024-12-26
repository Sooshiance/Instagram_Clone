from rest_framework import serializers

from .models import Follower, Notification

from user.models import User
from user.serializers import UserSerializer


class FollowerSerializer(serializers.ModelSerializer[Follower]):
    class Meta:
        model = Follower
        fields = ["pk", "follower", "following", "connected_at"]

    def validate(self, attrs: dict[str, str]) -> dict[str, str]:
        attrs = super().validate(attrs)
        follower: User = attrs.get("follower")
        following: User = attrs.get("following")

        if follower == following:
            raise serializers.ValidationError(
                "Follower and following cannot be the same user."
            )

        if not User.objects.filter(pk=follower.pk).exists():
            raise serializers.ValidationError("Follower user does not exist.")

        if not User.objects.filter(pk=following.pk).exists():
            raise serializers.ValidationError("Following user does not exist.")

        if following.is_private:
            raise serializers.ValidationError(
                "You cannot follow this user because his account is private."
            )

        return attrs


class NotificationSerializer(serializers.ModelSerializer[Notification]):
    receiver = UserSerializer(read_only=True)
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ["pk", "receiver", "sender"]
