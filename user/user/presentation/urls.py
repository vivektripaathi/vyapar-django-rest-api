from django.urls import path

from user.user.presentation.views import GetUserView, SendOTP

urlpatterns = [
    path("", GetUserView.as_view(), name="get_user"),
    path("send_otp/", SendOTP.as_view(), name="send_otp"),
]
