from rest_framework.exceptions import ValidationError

from .models import Follower, User


class FollowerRepository:
    @staticmethod
    def get_followers_of_user(user_id):
        """
        Returns a QuerySet of User instances who are followers of the given user.
        """
        return User.objects.filter(following_set__following_id=user_id)

    @staticmethod
    def get_following_of_user(user_id):
        """
        Returns a QuerySet of User instances who are being followed by the given user.
        """
        return User.objects.filter(follower_set__follower_id=user_id)
    
    @staticmethod
    def get_user_following(following_id):
        try:
            following = User.objects.get(pk=following_id)
            return following
        except User.DoesNotExist:
            raise ValidationError(detail=User.DoesNotExist)

    @staticmethod
    def create_follower(follower, following):
        """
        Creates a new follower relationship.
        """
        return Follower.objects.create(follower=follower, following=following)

    @staticmethod
    def remove_follower(follower, following):
        """
        Removes a follower relationship.
        """
        Follower.objects.filter(follower=follower, following=following).delete()
