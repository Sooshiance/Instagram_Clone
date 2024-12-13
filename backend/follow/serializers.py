from rest_framework import serializers

from .models import Follower

from user.models import User


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['pk', 'follower', 'following', 'connected_at']
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        follower = attrs.get('follower')
        following = attrs.get('following')

        if follower == following:
            raise serializers.ValidationError("Follower and following cannot be the same user.")

        if not User.objects.filter(pk=follower.pk).exists():
            raise serializers.ValidationError("Follower user does not exist.")

        if not User.objects.filter(pk=following.pk).exists():
            raise serializers.ValidationError("Following user does not exist.")
        
        if following.is_private:
            raise serializers.ValidationError("You cannot follow this user because his account is private.")

        return attrs
