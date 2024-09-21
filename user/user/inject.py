from dependency_injector import containers, providers

from user.user.data.abstract_repo import UserAbstractRepository
from user.user.data.db_repo import UserDbRepository

class UserSubAppContainer(containers.DeclarativeContainer):
    db_repo = providers.Dependency(
        instance_of=UserAbstractRepository,
        default=UserDbRepository(),
    )
