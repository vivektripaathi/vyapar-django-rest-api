import logging
import traceback
from typing import Dict, Union, cast

import jwt
import orjson
import pydantic
from django.conf import settings
from pydantic import BaseModel
from pydantic.generics import GenericModel
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler

from core.exceptions import InvalidTokenException, TokenExpiredException, VyaparAPIException, VyaparException

logger = logging.getLogger(__name__)


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


def custom_exception_handler(exc, context):
    """Custom exception handler for RDF views to handle cases like conversion of
    pydantic validation errors and so on."""

    # Convert pydantic validation errors to RDF validation errors
    if isinstance(exc, pydantic.ValidationError):
        error_dict = {}
        for err in exc.errors():
            # First lookup the elements in the path
            error_key = error_dict
            for part in err["loc"][:-1]:
                error_key_part = error_key.get(part, {})
                if not error_key_part or not isinstance(error_key_part, dict):
                    error_key[part] = {}
                error_key = error_key[part]

            # Set the error message on the final key in the path
            error_key[err["loc"][-1]] = [err["msg"]]
        exc = ValidationError(detail=error_dict).with_traceback(exc.__traceback__)

    # Call the base exception handler and return the response
    response = exception_handler(exc, context)

    if response is not None and response.status_code > 304:
        current_stack_trace = "".join(traceback.format_exception(exc.__class__, exc, exc.__traceback__))
        logger.info(
            "Response code %s from %s \n Stacktrace: %s",
            response.status_code,
            exc.__repr__(),
            current_stack_trace,
        )

    # Now add the HTTP status code to the response.
    if response is not None and isinstance(exc, VyaparAPIException):
        response.data["status_code"] = response.status_code
        response.data["code"] = exc.code if hasattr(exc, "code") else VyaparException.code
        response.data["message"] = response.data["detail"] if "detail" in response.data else ""

    return response


def create_jwt_token(payload: dict):
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")


def decode_jwt_token(token) -> dict:
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as exc:
        raise TokenExpiredException from exc
    except Exception as exc:
        raise InvalidTokenException from exc


def decode_expired_jwt_token(token: str) -> dict:
    try:
        return jwt.decode(token, options={"verify_signature": False})
    except Exception as exc:
        raise InvalidTokenException from exc
