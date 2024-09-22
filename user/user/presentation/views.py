import pydantic

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from dependency_injector.wiring import Provide

from user.types import UserId
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase


class GetUserView(APIView):
    def get(
        self,
        request,
        id: UserId,
        get_user_use_case: GetUserUseCase = Provide[
            "user.get_user_use_case"
        ],
    ):
        # print("got here")
        response = get_user_use_case.execute(id)
        return Response(response.dict_serialized(), status=status.HTTP_200_OK)
