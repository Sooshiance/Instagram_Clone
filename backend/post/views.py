from rest_framework import response, status, views, permissions
from rest_framework.exceptions import ValidationError

from .serializers import (
    PostSerializer,
    CommentSerializer
)
from .repositories import (
    PostRepository,
    CommentRepository,
)


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


class PostCommentView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        p = PostRepository.get_post_by_id(post_id=pk)
        cmt = CommentRepository.get_comments_by_post(post=p)
        srz = CommentSerializer(cmt, many=True)
        return response.Response(srz.data, status=status.HTTP_200_OK)


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


class CreateCommentView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = PostRepository.get_post_by_id(post_id=pk)

        body = request.data.get("body", None)
        comment = CommentRepository.create_comment(post, self.request.user, body)

        srz = CommentSerializer(comment)
        return response.Response(srz.data, status=status.HTTP_200_OK)


class LikePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        try:
            post = PostRepository.update_post_likes(pk, self.request.user)
            serializer = PostSerializer(post)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return response.Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        post = PostRepository.get_post_by_id(post_id=pk)
        caption = request.data.get("caption")
        location = request.data.get("location")
        post = PostRepository.update_post(pk, self.request.user, caption, location)
        srz = PostSerializer(post, many=False)
        return response.Response(srz.data, status=status.HTTP_200_OK)


class UpdateCommentView(views.APIView):
    permission_classes= [permissions.IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        body = request.data.get("body")
        updated_comment = CommentRepository.update_comment(self.request.user, comment_id=pk, body=body)
        srz = CommentSerializer(updated_comment)
        return response.Response(srz.data, status=status.HTTP_200_OK)


class DeletePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        PostRepository.delete_post(post_id=pk, user=self.request.user)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class DeleteComment(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        CommentRepository.delete_comment(pk, self.request.user)
        return response.Response(status=status.HTTP_204_NO_CONTENT)
