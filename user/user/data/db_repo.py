import logging

from user.exceptions import UserNotFound
from user.models import User
from user.types import UserId
from user.user.data.abstract_repo import UserAbstractRepository
from user.user.domain.domain_models import UserDomainModel

logger = logging.getLogger(__name__)


class UserDbRepository(UserAbstractRepository):
    """User Database Repository."""

    def _get(self, user_id: UserId) -> User:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist as exc:
            raise UserNotFound from exc

    def _get_by_contact_number(self, contact_number: str) -> User:
        try:
            return User.objects.get(contact_number=contact_number)
        except User.DoesNotExist as exc:
            raise UserNotFound from exc

    def get(self, id: UserId) -> UserDomainModel:
        """Get user by id"""
        logger.info("Getting user by id %s", id)
        user_db_entry = self._get(user_id=id)
        return UserDomainModel.from_orm(user_db_entry)

    def get_by_contact_number(self, contact_number: str) -> UserDomainModel:
        """Get user by contact number"""
        logger.info("Getting user by contact number %s", contact_number)
        user_db_entry = self._get_by_contact_number(contact_number=contact_number)
        return UserDomainModel.from_orm(user_db_entry)

    def create(self, user: UserDomainModel) -> UserDomainModel:
        """Create a new user."""
        logger.info("Creating new user with contact number %s", user.contact_number)

        user_db_entry = User.objects.create(
            name=user.name,
            contact_number=user.contact_number,
            aadhar_number=user.aadhar_number,
            pan_number=user.pan_number,
            is_setup_completed=user.is_setup_completed,
        )

        logger.info("Successfully created user with id %s", user_db_entry.id)
        return UserDomainModel.from_orm(user_db_entry)
