from dependency_injector import containers, providers

from user.user.data.abstract_repo import UserAbstractRepository
from user.user.data.db_repo import UserDbRepository
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase
from user.user.domain.use_cases.send_otp_use_case import SendOTPUseCase


class UserSubAppContainer(containers.DeclarativeContainer):
    db_repo = providers.Dependency(
        instance_of=UserAbstractRepository,
        default=UserDbRepository(),
    )
    get_user_use_case = providers.Factory(GetUserUseCase)
    send_otp_use_case = providers.Factory(SendOTPUseCase)
