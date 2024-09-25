from typing import Dict, Union, cast

import jwt
import orjson
from django.conf import settings
from pydantic import BaseModel
from pydantic.generics import GenericModel

from core.exceptions import InvalidTokenException, TokenExpiredException


def _dict_serialized(obj: Union[BaseModel, GenericModel], *args, **kwargs) -> Dict:
    """
    Returns a dict of serialized data. We need this because
    pydantic's .json() returns stringified json, we need
    a dict to return it as a response.
    """
    return cast(Dict, orjson.loads(obj.json(*args, **kwargs)))


class VyaparBaseModel(BaseModel):
    """Vyapar Base Model from which all other Models should inherit"""

    def dict_serialized(self, *args, **kwargs) -> Dict:
        return _dict_serialized(self, *args, **kwargs)


def decode_jwt_token(token) -> dict:
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as exc:
        raise TokenExpiredException from exc
    except Exception as exc:
        raise InvalidTokenException from exc
