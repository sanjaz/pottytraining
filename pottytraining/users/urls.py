from django.urls import include, path
from rest_framework import routers

from pottytraining.users.views import (
    AdminViewSet, ParentViewSet, TeacherViewSet, UserViewSet,
    user_create
)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet, basename="admins")
router.register(r'teachers', TeacherViewSet, basename="teachers")
router.register(r'parents', ParentViewSet, basename="parents")


urlpatterns = [
    path('users/create/', user_create, name="create_user"),
    path('', include(router.urls)),
]
