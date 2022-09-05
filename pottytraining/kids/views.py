from pottytraining.kids.serializers import KidSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from pottytraining.kids.filters import KidFilter
from pottytraining.kids.models import Kid, PeeOrPoo
from pottytraining.kids.serializers import KidSerializer, PeeOrPooSerializer


class KidViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = KidFilter
    queryset = Kid.objects.all()
    serializer_class = KidSerializer


class PeeOrPooViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PeeOrPoo.objects.all()
    serializer_class = PeeOrPooSerializer
