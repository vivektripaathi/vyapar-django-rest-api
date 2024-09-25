from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    inject_container = None

    def ready(self):
        from core import token
        from core.inject import CoreContainer

        self.inject_container = CoreContainer()
        self.inject_container.wire(
            packages=[token],
            modules=[],
        )
