from rest_framework.exceptions import ValidationError

from .models import Follower, User, Notification


class FollowerRepository:
    @staticmethod
    def get_followers_of_user(user_id):
        return User.objects.filter(following_set__following_id=user_id)

    @staticmethod
    def get_following_of_user(user_id):
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
        return Follower.objects.create(follower=follower, following=following)

    @staticmethod
    def remove_follower(follower, following):
        Follower.objects.filter(follower=follower, following=following).delete()


class NotificationRepositories:
    @staticmethod
    def ask_fellowships(receiver: User, sender: User):
        if receiver.is_private:
            if Follower.objects.filter(receiver, sender) is None:
                return Notification.objects.create(receiver, sender)
            else:
                raise ValidationError()
        else:
            raise ValidationError("How's that possible")

    @staticmethod
    def user_ask_for_following(receiver: User):
        return Notification.objects.filter(receiver=receiver)
