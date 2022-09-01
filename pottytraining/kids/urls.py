from posixpath import basename
from django.urls import include, path

from pottytraining.kids.views import KidViewSet
from pottytraining.routers import CustomRouter


router = CustomRouter()
router.register(r"kids", KidViewSet, basename="kids")


urlpatterns = [
    path("", include(router.urls)),
]
