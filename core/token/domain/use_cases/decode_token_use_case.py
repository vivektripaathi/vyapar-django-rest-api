import logging

from core.utils import decode_jwt_token

logger = logging.getLogger(__name__)


class DecodeTokenUseCase:
    def execute(
        self,
        token: str,
    ) -> dict:
        logger.info("Got request to decode token")
        return decode_jwt_token(token)
