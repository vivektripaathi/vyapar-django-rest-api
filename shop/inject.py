from dependency_injector import containers, providers

from shop.shop.inject import ShopSubAppContainer


class ShopContainer(containers.DeclarativeContainer):
    shop = providers.Container(ShopSubAppContainer)
