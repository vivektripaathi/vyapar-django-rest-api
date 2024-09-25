from dependency_injector import containers, providers

from core.token.inject import TokenSubAppContainer


class CoreContainer(containers.DeclarativeContainer):
    token = providers.Container(TokenSubAppContainer)
