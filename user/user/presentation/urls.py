from django.urls import path

from user.user.presentation.views import GetUserView


urlpatterns = [
    path(
        "<uuid:id>/",
        GetUserView.as_view(),
        name = "get_user"
    )
]