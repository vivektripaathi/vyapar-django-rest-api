import abc

from user.types import UserId
from user.user.domain.domain_models import UserDomainModel


class UserAbstractRepository(abc.ABC):
    """User Abstract Repository."""

    @abc.abstractmethod
    def get(self, id: UserId) -> UserDomainModel:
        """Get user by id"""
