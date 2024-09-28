import logging

from dependency_injector.wiring import Provide

from core.token.domain.use_cases.create_token_use_case import CreateTokenUseCase
from core.token.domain.use_cases.decode_token_use_case import DecodeTokenUseCase
from user.exceptions import UserNotFound, WrongOTPException
from user.user.domain.domain_models import UserDomainModel
from user.user.domain.use_cases.create_user_use_case import CreateUserUseCase
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase
from user.user.presentation.types import VerifyOTPRequest

logger = logging.getLogger(__name__)


class VerifyOTPUseCase:
    def __init__(
        self,
        decode_token_use_case: DecodeTokenUseCase = Provide["token.decode_token_use_case"],
        create_token_use_case: CreateTokenUseCase = Provide["token.create_token_use_case"],
        get_user_use_case: GetUserUseCase = Provide["user.get_user_use_case"],
        create_user_use_case: CreateUserUseCase = Provide["user.create_user_use_case"],
    ) -> None:
        self.decode_token_use_case = decode_token_use_case
        self.create_token_use_case = create_token_use_case
        self.get_user_use_case = get_user_use_case
        self.create_user_use_case = create_user_use_case

    def _verify_otp_with_token_request(self, verify_otp_request: VerifyOTPRequest, token_data: dict) -> UserDomainModel:
        if verify_otp_request.otp != token_data["otp"]:
            raise WrongOTPException("The provided OTP is incorrect.")

        contact_number = token_data["phone"]

        try:
            # Attempt to get the existing user by contact number
            user = self.get_user_use_case._get_user_by_contact_number(contact_number)
            return user
        except UserNotFound:
            # If the user is not found, create a new user
            new_user = UserDomainModel(
                name="Default Name",
                contact_number=contact_number,
                aadhar_number="",
                pan_number="",
                is_setup_completed=False,
            )
            created_user = self.create_user_use_case.execute(new_user)
            return created_user

    def execute(self, verify_otp_request: VerifyOTPRequest) -> dict:
        token_data = self.decode_token_use_case.execute(verify_otp_request.token)
        user = self._verify_otp_with_token_request(verify_otp_request, token_data)
        token = self.create_token_use_case.execute(user.dict_serialized())
        return {"user": user.dict_serialized(), "token": token}
