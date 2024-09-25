import logging

from core.utils import decode_expired_jwt_token

logger = logging.getLogger(__name__)


class DecodeExpiredTokenUseCase:
    def execute(
        self,
        token: str,
    ) -> dict:
        logger.info("Got request to decode an expired token")
        return decode_expired_jwt_token(token)
