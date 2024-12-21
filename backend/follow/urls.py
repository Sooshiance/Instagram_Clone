from django.urls import path

from .views import (
    PrivateProfileView,
    FollowerView,
    FollowUserView,
    CreateNotification,
    UserNotificationList,
)


app_name = 'follow'

urlpatterns = [
    path("profile/status/<str:pk>/", PrivateProfileView.as_view(), name=''),
    path("list/followers/", FollowerView.as_view(), name=''),
    path('follow/', FollowUserView.as_view(), name=''),
    path('un-follow/<int:following_id>/', FollowUserView.as_view(), name=''),
    path('send/notification/', CreateNotification.as_view(), name=''),
    path('see/user/ask/follow/list/', UserNotificationList.as_view(), name=''),
]
