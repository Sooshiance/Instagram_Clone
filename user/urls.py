from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='HOME'),
    path('login/', loginUser, name='LOGIN'),
    path('logout/', logoutUser, name='LOGOUT'),
    path('register/', registerUser, name='REGISTER'),
]
