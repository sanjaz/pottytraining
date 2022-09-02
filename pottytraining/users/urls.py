from django.urls import include, path

from pottytraining.routers import CustomRouter
from pottytraining.users.views import (
    AdminViewSet,
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
    path("", include(router.urls)),
]
