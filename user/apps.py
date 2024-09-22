from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    inject_container = None

    def ready(self) -> None:
        from user.inject import UserContainer
        from user import user

        self.inject_container = UserContainer()
        self.inject_container.wire(
            packages=[user],
            modules=[],
        )
