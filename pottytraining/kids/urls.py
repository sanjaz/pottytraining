from django.urls import include, path

from pottytraining.kids.views import KidViewSet, PeeOrPooViewSet
from pottytraining.routers import NestedRouter


router = NestedRouter()
router.register(
    r'kids', KidViewSet, basename='kids'
).register(
    r'pee-or-poos', PeeOrPooViewSet, basename='kid_pee_or_poos',
    parents_query_lookups=['kid']
)


urlpatterns = [
    path("", include(router.urls)),
]
