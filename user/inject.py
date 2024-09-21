from dependency_injector import containers, providers

from user.user.inject import UserSubAppContainer


class UserContainer(containers.DeclarativeContainer):
    user = providers.Container(UserSubAppContainer)
