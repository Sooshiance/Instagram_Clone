from django.urls import path

from .views import (
    UserPostsView,
    SinglePostView,
    CreatePostView,
    CreateCommentView,
    LikePostView,
    UpdatePostView,
    UpdateCommentView,
    DeletePostView,
    DeleteComment,
)


app_name = 'post'

urlpatterns = [
    path("create/post/", CreatePostView.as_view(), name=''),
    path("create/like/post/<int:pk>/", LikePostView.as_view(), name=''),
    path("create/comment/post/<int:pk>/", CreateCommentView.as_view(), name=''),
    path("view/post/", UserPostsView.as_view(), name=''),
    path("view/post/<int:pk>/", SinglePostView.as_view(), name=''),
    path("update/post/<int:pk>/", UpdatePostView.as_view(), name=''),
    path("update/comment/<int:pk>/", UpdateCommentView.as_view(), name=''),
    path("delete/post/<int:pk>/", DeletePostView.as_view(), name=''),
    path("delete/comment/<int:pk>/", DeleteComment.as_view(), name=''),
]
