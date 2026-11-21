from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .serializers import UserSerializer  # noqa: F401  (供 urls 引用检查)

router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("template/list/", views.user_list, name="user-list-template"),
    path("template/me/", views.user_me, name="user-me-template"),
]
