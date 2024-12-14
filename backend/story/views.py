from rest_framework import views, response, status, permissions

from .repositories import StoryRepositories
from .serializers import StorySerializer