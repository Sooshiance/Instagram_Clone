from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, permissions, generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User,Profile
from .serializers import (RegisterSerializer,
                          UserSerializer,
                          CustomTokenObtainPairSerializer,
                          ProfileSerializer,)
from .services import UserService


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user:User = UserService.register_user(serializer.validated_data['username'], serializer.validated_data['password'])
            srz = UserSerializer(user)
            return Response({"message": srz.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(APIView):
    def post(self, request):
        user = UserService.get_user_by_username(request.data['username'])
        if user:
            UserService.create_password_reset_otp(user)
            return Response({"message": "Password reset OTP sent"}, status=status.HTTP_200_OK)
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class VerifyOTPView(APIView):
    def post(self, request):
        user = UserService.get_user_by_username(request.data['username'])
        if user and UserService.verify_otp(user, request.data['otp']):
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    def post(self, request):
        if UserService.reset_password(request.data['username'], request.data['otp'], request.data['new_password']):
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid OTP or username"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            user = self.request.user
            my_user = User.objects.get(username=user)
            profile = Profile.objects.get(user=my_user)
            return profile
        except Exception as e:
            ValidationError(str(e))


class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        profile = self.request.user.profile
        srz = ProfileSerializer(profile, data=request.data, partial=True)
        if not srz.is_valid():
            print(srz.errors)
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)
        srz.save()
        return Response(srz.data, status=status.HTTP_200_OK)
