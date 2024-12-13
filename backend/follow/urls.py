from django.urls import path

from .views import (
    FollowerView,
    FollowUserView,
)


app_name = 'follow'

urlpatterns = [
    path("followers/", FollowerView.as_view(), name=''),
    path('follow/', FollowUserView.as_view(), name=''),
    path('un-follow/<int:following_id>/', FollowUserView.as_view(), name=''),
]
