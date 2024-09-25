import uuid

from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True, primary_key=True
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    contact_number = models.CharField(max_length=255, null=False, blank=False)
    aadhar_number = models.CharField(max_length=255, null=False, blank=False)
    pan_number = models.CharField(max_length=255, null=False, blank=False)
    is_setup_completed = models.BooleanField(default=False)

    class Meta:
        db_table = "users"

    @property
    def is_authenticated(self):
        """
        Always return True.
        This is a way to tell if the user has been authenticated in templates.
        """
        return True
