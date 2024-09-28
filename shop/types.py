from typing import NewType

from pydantic import UUID4

ShopCategoryId = NewType("ShopCategoryId", UUID4)
ShopId = NewType("ShopId", UUID4)
