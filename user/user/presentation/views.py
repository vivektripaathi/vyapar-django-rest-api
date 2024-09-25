from dependency_injector.wiring import Provide
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.auth import JWTBearerTokenAuthentication
from core.request_types import VyaparAuthenticatedHttpRequest
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase
from user.user.domain.use_cases.send_otp_use_case import SendOTPUseCase


class SendOTP(APIView):
    def post(self, request):
        phone = request.data.get("phone")

        if not phone or len(phone) != 10:
            return Response(
                {"error": "Phone number is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            send_otp_use_case = SendOTPUseCase()
            token = send_otp_use_case.execute(phone)

            return Response({"token": token}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


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
