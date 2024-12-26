from rest_framework import views, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request

from .repositories import (
    FollowerRepository,
    NotificationRepositories,
)
from .serializers import FollowerSerializer, NotificationSerializer

from user.models import User
from user.serializers import UserSerializer


class PrivateProfileView(views.APIView):
    """
    `Users` can see other `Profiles`
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(
        self, request: Request, pk: str, *args: list[str], **kwargs: dict[str, str]
    ) -> Response:
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist as e:
            raise ValidationError(str(e))
        if user.is_private:
            return Response(
                data={"error": "Profile is private"}, status=status.HTTP_204_NO_CONTENT
            )
        user_srz = UserSerializer(user)
        return Response(data=user_srz.data, status=status.HTTP_200_OK)


class FollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(
        self, request: Request, pk: str, *args: list[str], **kwargs: dict[str, str]
    ) -> Response:
        followers = FollowerRepository.get_followers_of_user(self.request.user.pk)
        following = FollowerRepository.get_following_of_user(self.request.user.pk)
        follower_serializer = UserSerializer(followers, many=True)
        following_serializer = UserSerializer(following, many=True)
        response_data = {
            "followers": follower_serializer.data,
            "following": following_serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class FollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(
        self, request: Request, pk: str, *args: list[str], **kwargs: dict[str, str]
    ) -> Response:
        following_id = request.data.get("following_id")
        follower = self.request.user

        try:
            following = User.objects.get(pk=following_id, is_private=False)
        except User.DoesNotExist:
            return Response(
                {"detail": "User to follow does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            follower_instance = FollowerRepository.create_follower(
                follower=follower, following=following
            )
            serializer = FollowerSerializer(follower_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        following_id = request.data.get("following_id")
        follower = self.request.user

        try:
            following = User.objects.get(pk=following_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User to unfollow does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        FollowerRepository.remove_follower(follower=follower, following=following)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateNotification(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        receiver_pk = request.data.get("pk", None)
        try:
            receiver = User.objects.get(pk=receiver_pk)
        except User.DoesNotExist as e:
            raise ValidationError(str(e))
        sender = self.request.user
        NotificationRepositories.ask_fellowships(receiver, sender)
        srz = NotificationSerializer(receiver, sender)
        return Response(srz.data)


class UserNotificationList(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_list = NotificationRepositories.user_ask_for_following(self.request.user)
        srz = UserSerializer(user_list, many=True)
        return Response(srz.data)
