from decimal import Decimal
from typing import Optional, Tuple

from core.utils import VyaparBaseModel
from shop.types import ShopCategoryId, ShopId
from user.types import UserId
from user.user.domain.domain_models import UserDomainModel


class ShopCategoryDomainModel(VyaparBaseModel):
    id: ShopCategoryId
    name: str

    class Config:
        orm_mode = True


class ShopDomainModel(VyaparBaseModel):
    id: ShopId
    name: str
    description: Optional[str]
    address: Optional[str]
    location: Tuple[Decimal, Decimal]
    gst_number: Optional[str]
    invoice: Optional[str]
    shop_image: Optional[str]
    category_id: Optional[ShopCategoryId]
    category: Optional[ShopCategoryDomainModel]
    owner_id: Optional[UserId]
    owner: UserDomainModel

    class Config:
        orm_mode = True
