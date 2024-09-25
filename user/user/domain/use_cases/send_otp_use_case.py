from django.http import JsonResponse
from .models import User
import random
import jwt
from django.conf import settings
from datetime import datetime, timedelta, timezone


class SendOTPUseCase:
    def execute(self, phone) -> str:
        otp = random.randint(1000, 9999)
        data = {
            "phone": phone,
            "otp": otp,
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=10),  # Token expires in 10 minutes
        }
        encoded_jwt = jwt.encode(data, settings.JWT_SECRET, algorithm="HS256")
        # send_otp_to_phone(phone, otp) #Abstract Function
        return encoded_jwt