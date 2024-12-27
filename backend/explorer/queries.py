from datetime import datetime

from django.db.models import Count
from django.utils.timezone import timedelta

from post.models import Post


class PostQueries:
    @staticmethod
    def get_posts_with_counts():
        posts = Post.objects.annotate(
            likes_count=Count("likes"), views_count=Count("views")
        ).values("pk", "likes_count", "views_count", "caption")

        return posts

    @staticmethod
    def get_posts_with_counts_in_one_day(
        time_period: timedelta, created_at: datetime
    ) -> Post:
        start_time = created_at + timedelta(days=1) - timedelta(microseconds=1)

        posts = (
            Post.objects.filter(updated_at__range=(created_at, start_time))
            .annotate(likes_count=Count("likes"), views_count=Count("views"))
            .values("pk", "likes_count", "views_count", "caption")
        )

        return posts
