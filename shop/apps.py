from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop"
    inject_container = None

    def ready(self) -> None:
        from shop import shop
        from shop.inject import ShopContainer

        self.inject_container = ShopContainer()
        self.inject_container.wire(
            packages=[shop],
            modules=[],
        )
