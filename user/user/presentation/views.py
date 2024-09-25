from dependency_injector.wiring import Provide
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.auth import JWTBearerTokenAuthentication
from core.request_types import VyaparAuthenticatedHttpRequest, VyaparHttpRequest
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase
from user.user.domain.use_cases.send_otp_use_case import SendOTPUseCase
from user.user.domain.use_cases.verify_otp_use_case import VerifyOTPUseCase
from user.user.presentation.types import SendOTPRequest, VerifyOTPRequest


class SendOTP(APIView):
    def post(
        self,
        request: VyaparHttpRequest,
        send_otp_use_case: SendOTPUseCase = Provide["user.send_otp_use_case"],
    ):
        send_otp_request = SendOTPRequest.parse_obj(request.data)
        response = send_otp_use_case.execute(send_otp_request)
        return Response(response.dict_serialized(), status=status.HTTP_200_OK)


class VerifyOTP(APIView):
    def post(
        self,
        request: VyaparHttpRequest,
        verify_otp_use_case: VerifyOTPUseCase = Provide["user.verify_otp_use_case"],
    ):
        verify_otp_request = VerifyOTPRequest.parse_obj(request.data)
        response = verify_otp_use_case.execute(verify_otp_request)
        return Response(response, status=status.HTTP_200_OK)


class GetUserView(APIView):
    authentication_classes = [JWTBearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(
        self,
        request: VyaparAuthenticatedHttpRequest,
        get_user_use_case: GetUserUseCase = Provide["user.get_user_use_case"],
    ):
        response = get_user_use_case.execute(request.user.id)
        return Response(response.dict_serialized(), status=status.HTTP_200_OK)
