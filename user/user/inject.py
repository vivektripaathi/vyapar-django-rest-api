from dependency_injector import containers, providers

from user.user.data.abstract_repo import UserAbstractRepository
from user.user.data.db_repo import UserDbRepository
from user.user.domain.use_cases.create_user_use_case import CreateUserUseCase
from user.user.domain.use_cases.get_user_use_case import GetUserUseCase
from user.user.domain.use_cases.send_otp_use_case import SendOTPUseCase
from user.user.domain.use_cases.verify_otp_use_case import VerifyOTPUseCase


class UserSubAppContainer(containers.DeclarativeContainer):
    db_repo = providers.Dependency(
        instance_of=UserAbstractRepository,
        default=UserDbRepository(),
    )
    get_user_use_case = providers.Factory(GetUserUseCase)
    send_otp_use_case = providers.Factory(SendOTPUseCase)
    verify_otp_use_case = providers.Factory(VerifyOTPUseCase)
    create_user_use_case = providers.Factory(CreateUserUseCase)
