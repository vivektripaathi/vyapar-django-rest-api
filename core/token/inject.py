from dependency_injector import containers, providers

from core.token.domain.use_cases.create_token_use_case import CreateTokenUseCase
from core.token.domain.use_cases.decode_expired_token_use_case import DecodeExpiredTokenUseCase
from core.token.domain.use_cases.decode_token_use_case import DecodeTokenUseCase


class TokenSubAppContainer(containers.DeclarativeContainer):
    create_token_use_case = providers.Factory(CreateTokenUseCase)
    decode_token_use_case = providers.Factory(DecodeTokenUseCase)
    decode_expired_token_use_case = providers.Factory(DecodeExpiredTokenUseCase)
