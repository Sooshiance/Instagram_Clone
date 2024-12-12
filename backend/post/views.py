from rest_framework import response, status, views, permissions

from .serializers import (
    PostSerializer,
    CommentSerializer
)
from .repositories import (
    PostRepository,
    CommentRepository,
)


class CreatePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        caption = request.data.get('caption')
        location = request.data.get('location')
        images = request.FILES.getlist('images')
        if not images:
            return response.Response({"error": "No images provided."}, status=status.HTTP_400_BAD_REQUEST)
        post = PostRepository.create_post(user, caption, images, location)
        post_serializer = PostSerializer(post)
        return response.Response(post_serializer.data, status=status.HTTP_201_CREATED)


class UserPostsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        post = PostRepository.get_post_by_user(user=self.request.user)
        post_srz = PostSerializer(post, many=True)
        return response.Response(post_srz.data, status=status.HTTP_200_OK)


class SinglePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        p = PostRepository.get_post_by_id(post_id=pk)
        srz = PostSerializer(p, many=False)
        return response.Response(srz.data, status=status.HTTP_200_OK)
