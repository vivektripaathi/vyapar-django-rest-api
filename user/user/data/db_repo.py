import logging

from user.models import User
from user.types import UserId
from user.user.data.abstract_repo import UserAbstractRepository
from user.user.domain.domain_models import UserDomainModel

logger = logging.getLogger(__name__)

class UserDbRepository(UserAbstractRepository):
    """User Database Repository."""

    def get(self, id: UserId) -> UserDomainModel:
        """Get user by id"""
        logger.info("Getting user by id %s", id)
        user_db_entry = User.objects.get(id=id)
        return UserDomainModel.from_orm(user_db_entry)
