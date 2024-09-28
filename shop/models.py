from django.contrib.postgres.fields import ArrayField
from django.db import models

from core.model_mixins import UUIDPrimaryKeyMixin


class ShopCategory(UUIDPrimaryKeyMixin):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = '"vyapar"."shop_categories"'


class Shop(UUIDPrimaryKeyMixin):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    location = ArrayField(models.DecimalField(max_digits=9, decimal_places=6), size=2)
    gst_number = models.CharField(null=True, blank=True, max_length=15)
    invoice = models.TextField(null=True, blank=True)
    shop_image = models.TextField(null=True, blank=True)
    category = models.ForeignKey(ShopCategory, related_name="shop_categories", on_delete=models.PROTECT)
    created_by = models.ForeignKey(
        "user.User",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="%(class)s_created_by",
    )

    class Meta:
        db_table = '"vyapar"."shops"'
