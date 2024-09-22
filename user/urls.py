from django.urls import include, path

from user.user.presentation import urls as user_urls

app_name = "user"

urlpatterns = [
    path("", include(user_urls)),
]
