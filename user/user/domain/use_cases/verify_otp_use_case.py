import random

from dependency_injector.wiring import Provide

from core.token.domain.use_cases.decode_token_use_case import DecodeTokenUseCase
from user.user.presentation.types import VerifyOTPRequest


class VerifyOTPUseCase:
    def __init__(
        self,
        decode_token_use_case: DecodeTokenUseCase = Provide[
            "token.decode_token_use_case"
        ],
    ) -> None:
        self.decode_token_use_case = decode_token_use_case

    def _verify_otp_with_token_request(self, verify_otp_request: VerifyOTPRequest, token_data: dict) -> dict:
        if verify_otp_request.otp != token_data["otp"]:
            return {"error": "Wrong OTP"}
        return {"success": "OTP verified"}

    def execute(self, verify_otp_request: VerifyOTPRequest) -> dict:
        token_data = self.decode_token_use_case.execute(verify_otp_request.token)
        otp_response = self._verify_otp_with_token_request(verify_otp_request, token_data)
        return otp_response
