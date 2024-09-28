import logging

from dependency_injector.wiring import Provide
from user.user.data.abstract_repo import UserAbstractRepository
from user.user.domain.domain_models import UserDomainModel
from user.exceptions import UserAlreadyExists, UserNotFound
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase

logger = logging.getLogger(__name__)


class CreateUserUseCase:
    def __init__(
            self,
            db_repo: UserAbstractRepository = Provide["user.db_repo"],
            get_user_use_case: GetUserUseCase = Provide["user.get_user_use_case"],
            ) -> None:
        self.db_repo = db_repo
        self.get_user_use_case = get_user_use_case

    def execute(self, user: UserDomainModel) -> UserDomainModel:
        try:
            existing_user = self.get_user_use_case._get_user_by_contact_number(user.contact_number)
            if existing_user:
                raise UserAlreadyExists(f"User with contact number {user.contact_number.value} already exists.")
        except UserNotFound:
            created_user = self.db_repo.create(user)
            logger.info("User created successfully with id %s", created_user.id)
            return created_user
