import random

from dependency_injector.wiring import Provide

from core.token.domain.use_cases.create_token_use_case import CreateTokenUseCase
from user.user.presentation.types import SendOTPRequest


class SendOTPUseCase:
    def __init__(
        self,
        create_token_use_case: CreateTokenUseCase = Provide["token.create_token_use_case"],
    ) -> None:
        self.create_token_use_case = create_token_use_case

    def _get_token_request(self, otp_request: SendOTPRequest) -> dict:
        otp: int = random.randint(100000, 999999)
        print(otp)
        return {
            "phone": otp_request.phone,
            "otp": otp,
        }

    def execute(self, otp_request: SendOTPRequest) -> str:
        token_request = self._get_token_request(otp_request)
        encoded_jwt = self.create_token_use_case.execute(token_request)
        # TODO: send_otp_to_phone(phone, otp) #Abstract Function
        return encoded_jwt
