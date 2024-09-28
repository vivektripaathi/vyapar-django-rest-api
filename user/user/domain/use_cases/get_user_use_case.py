import logging

from dependency_injector.wiring import Provide

from user.types import UserId
from user.user.data.abstract_repo import UserAbstractRepository
from user.user.domain.domain_models import UserDomainModel

logger = logging.getLogger(__name__)


class GetUserUseCase:
    def __init__(self, db_repo: UserAbstractRepository = Provide["user.db_repo"]) -> None:
        self.db_repo = db_repo

    def _get_user_by_contact_number(self, contact_number: str) -> UserDomainModel:
        logger.info("Getting user by contact number %s", contact_number)
        return self.db_repo.get_by_contact_number(contact_number)

    def execute(self, id: UserId) -> UserDomainModel:
        logger.info("Got request to get user by id %s", id)
        return self.db_repo.get(id)
