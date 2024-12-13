from rest_framework import views, status, permissions
from rest_framework.response import Response

from .repositories import FollowerRepository
from .serializers import FollowerSerializer

from user.models import User
from user.serializers import UserSerializer


class FollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get followers and following
        followers = FollowerRepository.get_followers_of_user(self.request.user.pk)
        following = FollowerRepository.get_following_of_user(self.request.user.pk)

        # Serialize followers and following
        follower_serializer = UserSerializer(followers, many=True)
        following_serializer = UserSerializer(following, many=True)

        # Prepare response data
        response_data = {
            'followers': follower_serializer.data,
            'following': following_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class FollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        following_id = request.data.get('following_id')
        follower = self.request.user
        
        try:
            following = User.objects.get(pk=following_id, is_private=False)
        except User.DoesNotExist:
            return Response({"detail": "User to follow does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Create a new follower relationship
        try:
            follower_instance = FollowerRepository.create_follower(follower=follower, following=following)
            serializer = FollowerSerializer(follower_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        following_id = request.data.get('following_id')
        follower = self.request.user 
        
        try:
            following = User.objects.get(pk=following_id)
        except User.DoesNotExist:
            return Response({"detail": "User to unfollow does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Remove the follower relationship
        FollowerRepository.remove_follower(follower=follower, following=following)
        return Response(status=status.HTTP_204_NO_CONTENT)
