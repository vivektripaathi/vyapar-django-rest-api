from rest_framework import status

from core.exceptions import VyaparException


class UserNotFound(VyaparException):
    code = "Vyapar_USER_0001"
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Requested user does not exist"
