from dependency_injector import containers, providers

from shop.shop.data.abstract_repo import ShopAbstractRepository
from shop.shop.data.db_repo import ShopDbRepository


class ShopSubAppContainer(containers.DeclarativeContainer):
    db_repo = providers.Dependency(
        instance_of=ShopAbstractRepository,
        default=ShopDbRepository(),
    )
