from user.models import User
from user.types import UserId
from user.user.data.abstract_repo import UserAbstractRepository
from user.user.domain.domain_models import UserDomainModel

class UserDbRepository(UserAbstractRepository):
    """User Database Repository."""

    def get(self, id: UserId) -> UserDomainModel:
        """Get user by id"""
        user_db_entry = User.objects.get(id=id)
        return UserDomainModel.from_orm(user_db_entry)
