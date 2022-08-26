from django.urls import include, path

from pottytraining.users.routers import CustomRouter
from pottytraining.users.views import (
    AdminViewSet,
    CreateUserView,
    ParentViewSet,
    TeacherViewSet,
    UserViewSet,
)


router = CustomRouter()
router.register(r"users", UserViewSet)
router.register(r"admins", AdminViewSet, basename="admins")
router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r"parents", ParentViewSet, basename="parents")


urlpatterns = [
    path("users/create/v1/", CreateUserView.as_view(), name="create_user"),
    path("", include(router.urls)),
]
