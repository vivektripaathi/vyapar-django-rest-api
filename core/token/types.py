from datetime import datetime

from core.utils import VyaparBaseModel


class TokenResponse(VyaparBaseModel):
    token: str
    expires_in: datetime


class TokenRequest(VyaparBaseModel):
    token: str
