from rest_framework.exceptions import ValidationError

from .models import OTP, User


class UserRepository:
    @staticmethod
    def create_user(**kwargs):
        return User.objects.create_user(**kwargs)

    @staticmethod
    def get_user_by_username(username):
        try:
            return User.objects.get(username=username)
        except Exception as e:
            raise ValidationError(e)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(pk=user_id)
        except Exception as e:
            raise ValidationError(e)


class OTPRepository:
    @staticmethod
    def create_otp(user, otp):
        return OTP.objects.create(user=user, otp=otp)

    @staticmethod
    def get_otp(user, otp):
        return OTP.objects.filter(user=user, otp=otp).first()


class PasswordResetTokenRepository:
    @staticmethod
    def create_token(user, token, expires_at):
        return OTP.objects.create(user=user, otp=token, expires_at=expires_at)

    @staticmethod
    def get_token(token):
        return OTP.objects.filter(otp=token).first()
