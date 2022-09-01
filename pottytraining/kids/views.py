from pottytraining.kids.serializers import KidSerializer
from rest_framework import viewsets

from pottytraining.kids.models import Kid
from pottytraining.kids.serializers import KidSerializer


class KidViewSet(viewsets.ModelViewSet):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer
