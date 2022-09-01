from pottytraining.kids.serializers import KidSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets

from pottytraining.kids.filters import KidFilter
from pottytraining.kids.models import Kid
from pottytraining.kids.serializers import KidSerializer


class KidViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = KidFilter
    queryset = Kid.objects.all()
    serializer_class = KidSerializer
