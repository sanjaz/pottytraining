from django.urls import include, path
from rest_framework import routers

from pottytraining.users.views import (
    AdminViewSet, ParentViewSet, TeacherViewSet, UserViewSet
)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet, basename="admins")
router.register(r'teachers', TeacherViewSet, basename="teachers")
router.register(r'parents', ParentViewSet, basename="parents")


urlpatterns = [
    path('', include(router.urls)),
]
