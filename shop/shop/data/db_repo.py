import logging

from shop.models import Shop
from shop.shop.data.abstract_repo import ShopAbstractRepository
from shop.shop.domain.domain_models import ShopDomainModel

logger = logging.getLogger(__name__)


class ShopDbRepository(ShopAbstractRepository):
    """Shop Database Repository"""

    def create(self, shop: ShopDomainModel) -> ShopDomainModel:
        """Create a shop"""
        logger.info("Creating shop with owner id%s", shop.owner_id)
        shop_entry = Shop.objects.create(
            id=shop.id,
            name=shop.name,
            description=shop.description,
            address=shop.address,
            locations=shop.location,
            gst_number=shop.gst_number,
            invoice=shop.invoice,
            shop_image=shop.shop_image,
            category_id=shop.category_id,
            owner_id=shop.owner_id,
        )
        return ShopDomainModel.from_orm(shop_entry)
