import logging
import uuid

from django.db import models

logger = logging.getLogger(__name__)


class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True, primary_key=True)

    class Meta:
        abstract = True
