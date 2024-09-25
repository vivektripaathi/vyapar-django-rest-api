import jwt
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from core.exceptions import InvalidTokenException, TokenExpiredException
from core.utils import decode_jwt_token
from user.exceptions import UserNotFound
from user.models import User


class JWTBearerTokenAuthentication(BaseAuthentication):
    keyword = "Bearer"

    def _get_token(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        if len(auth) == 1:
            msg = _("Invalid token header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _("Invalid token header. Token string should not contain spaces.")
            raise exceptions.AuthenticationFailed(msg)
        try:
            token = auth[1].decode()
        except UnicodeError as exc:
            msg = _("Token string should not contain invalid characters.")
            raise exceptions.AuthenticationFailed(msg) from exc
        return token

    def authenticate(self, request):
        token = self._get_token(request)
        if not token:
            return None, None
        try:
            decoded_token = decode_jwt_token(token)
        except jwt.ExpiredSignatureError as exc:
            raise TokenExpiredException("Auth Token has been expired") from exc
        except jwt.InvalidTokenError as exc:
            raise InvalidTokenException from exc

        try:
            user = User.objects.get(id=decoded_token["sub"])
        except User.DoesNotExist as exc:
            raise UserNotFound from exc

        return (user, token)
