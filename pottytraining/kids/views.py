from pottytraining.kids.serializers import KidSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pottytraining.kids.filters import KidFilter
from pottytraining.kids.models import Kid, PeeOrPoo
from pottytraining.kids.serializers import KidSerializer, PeeOrPooSerializer


class KidViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = KidFilter
    queryset = Kid.objects.all()
    serializer_class = KidSerializer

    @action(detail=True,
            url_path="pee_or_poos",
            url_name="kid_pee_or_poos")
    def list_pee_or_poos(self, request, pk=None):
        pee_or_poos = PeeOrPoo.objects.filter(kid_id=pk)
        serializer = PeeOrPooSerializer(
            pee_or_poos, many=True, context={"request": request}
        )
        return Response(serializer.data)
