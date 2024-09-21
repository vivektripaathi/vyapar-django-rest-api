from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    inject_container = None

    def ready(self) -> None:
        from user.inject import UserContainer

        self.inject_container = UserContainer()
        self.inject_container.wire(
            packages=[],
            modules=[],
        )
