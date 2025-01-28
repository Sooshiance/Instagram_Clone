import uuid

from .models import User
from .repositories import OTPRepository, UserRepository
from .utils import checkUsername, sendEmailOTP, sendPhoneOTP


class UserService:
    @staticmethod
    def get_user_by_pk(user: User):
        return UserRepository.get_user_by_id(user.pk)

    @staticmethod
    def get_user_by_username(username):
        return UserRepository.get_user_by_username(username)

    @staticmethod
    def register_user(username, password):
        user_type = checkUsername(username)
        user: User = UserRepository.create_user(username=username, password=password)
        user.set_password(password)
        if user_type == "phone":
            user.is_phone = True
        elif user_type == "email":
            user.is_email = True
        user.save()
        return user

    @staticmethod
    def send_otp(user: User):
        otp = str(uuid.uuid4().int)[:6]
        print(f"The OTP ===== {otp}")
        OTPRepository.create_otp(user, otp)
        if user.is_phone:
            sendPhoneOTP(user)
        elif user.is_email:
            sendEmailOTP(user)

    @staticmethod
    def verify_otp(user, otp):
        otp_record = OTPRepository.get_otp(user, otp)
        return otp_record

    @staticmethod
    def create_password_reset_otp(user: User):
        otp = str(uuid.uuid4().int)[:6]
        print(f"OTP ================ {otp}")
        OTPRepository.create_otp(user, otp)
        if user.is_phone:
            sendPhoneOTP(user)
        elif user.is_email:
            sendEmailOTP(user)
        return otp

    @staticmethod
    def reset_password(username, otp, new_password):
        user = UserRepository.get_user_by_username(username)
        if user and UserService.verify_otp(user, otp):
            user.set_password(new_password)
            user.save()
            return True
        return False
