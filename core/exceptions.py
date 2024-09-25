from rest_framework import status
from rest_framework.exceptions import APIException


class VyaparAPIException(APIException):
    pass


class VyaparException(VyaparAPIException):
    """
    Base class for Vyapar's REST framework exceptions.
    Subclasses should provide `.status_code`, `.code`  and `.default_detail` properties.
    """

    code = "VYAPAR_ERROR_00000"


class TokenExpiredException(VyaparException):
    code = "CORE_00001"
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Token is expired"


class InvalidTokenException(VyaparException):
    code = "CORE_00002"
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Token is not Valid"
