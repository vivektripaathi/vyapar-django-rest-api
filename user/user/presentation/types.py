from pydantic import root_validator

from core.utils import VyaparBaseModel


class SendOTPRequest(VyaparBaseModel):
    phone: str

    @root_validator()
    def validate_phone(cls, values):
        if values.get("phone"):
            password_length = len(values["phone"])
            if password_length != 10:
                raise ValueError("Phone must be of length 10")
        return values
