import logging

from dependency_injector.wiring import Provide

from user.types import UserId
from user.user.data.abstract_repo import UserAbstractRepository
from user.user.domain.domain_models import UserDomainModel

logger = logging.getLogger(__name__)

class GetUserUseCase:
    def __init__(
        self, db_repo: UserAbstractRepository = Provide["user.db_repo"]
    ) -> None:
        self.db_repo = db_repo

    def execute(self, id: UserId) -> UserDomainModel:
        logger.info(
            "Got request to get user by id %s", id
        )
        return self.db_repo.get(id)
