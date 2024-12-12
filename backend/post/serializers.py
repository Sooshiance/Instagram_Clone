from rest_framework import serializers

from .models import (
    Post,
    Comment,
    Album
)

from user.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = [
            'pk',
            'post',
            'image',
            ]


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    album = AlbumSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            'pk',
            'user',
            'caption',
            'likes',
            'created_at',
            'updated_at',
            'location',
            'album',
        ]


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'pk',
            'post',
            'user',
            'body',
            'created_at',
            'updated_at',
            ]
