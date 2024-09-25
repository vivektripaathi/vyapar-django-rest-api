from django.urls import path

from user.user.presentation.views import GetUserView, SendOTP, VerifyOTP

urlpatterns = [
    path("", GetUserView.as_view(), name="get_user"),
    path("send_otp/", SendOTP.as_view(), name="send_otp"),
    path("verify_otp/", VerifyOTP.as_view(), name="verify_otp"),
]
