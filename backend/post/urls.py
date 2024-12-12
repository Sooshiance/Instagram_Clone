from django.urls import path

from .views import (
    CreatePostView,
    UserPostsView,
    SinglePostView,
)


app_name=''

urlpatterns = [
    path("post/create/", CreatePostView.as_view(), name=''),
    path("post/user/view/", UserPostsView.as_view(), name=''),
    path("post/user/<int:pk>/", SinglePostView.as_view(), name=''),
]
