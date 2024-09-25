from typing import Any, Union

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.http import HttpRequest

from user.models import User


class VyaparHttpRequest(HttpRequest):
    user: Union[AbstractBaseUser, AnonymousUser]
    # shop: Optional[Shop]
    data: Any


class VyaparAuthenticatedHttpRequest(VyaparHttpRequest):
    user: User
    # shop: Optional[Shop]
    data: Any
