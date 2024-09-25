from dependency_injector.wiring import Provide
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.request_types import VyaparAuthenticatedHttpRequest
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase


class GetUserView(APIView):
    def get(
        self,
        request: VyaparAuthenticatedHttpRequest,
        get_user_use_case: GetUserUseCase = Provide["user.get_user_use_case"],
    ):
        response = get_user_use_case.execute(request.user.id)
        return Response(response.dict_serialized(), status=status.HTTP_200_OK)
