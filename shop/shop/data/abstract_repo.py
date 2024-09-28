import abc

from shop.shop.domain.domain_models import ShopDomainModel


class ShopAbstractRepository(abc.ABC):
    """Shop Abstract Repository."""

    @abc.abstractmethod
    def create(self, shop: ShopDomainModel) -> ShopDomainModel:
        """Create a shop"""
