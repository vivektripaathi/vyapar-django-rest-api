import logging
from datetime import datetime, timedelta, timezone

from django.conf import settings

from core.token.types import TokenResponse
from core.utils import create_jwt_token

logger = logging.getLogger(__name__)


class CreateTokenUseCase:
    def execute(
        self,
        token_request: dict,
    ):
        logger.info("Got request to generate a encoded token")
        expiry = datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_EXPIRY_MINUTES
        )
        token_request["exp"] = expiry
        token = create_jwt_token(token_request)
        return TokenResponse(token=token, expires_in=expiry)
