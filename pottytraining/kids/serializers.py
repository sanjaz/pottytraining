from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from pottytraining.kids.models import Kid, PeeOrPoo


class PeeOrPooHyperlink(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {"parent_lookup_kid": obj.kid.id, "pk": obj.pk}
        return reverse(
            view_name, kwargs=url_kwargs, request=request, format=format
        )


class PeeOrPooSerializer(serializers.ModelSerializer):
    url = PeeOrPooHyperlink(read_only=True, view_name="pee_or_poos-detail")

    class Meta:
        model = PeeOrPoo
        fields = ["id", "url", "is_poo", "time", "note"]


class KidSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(
        source="guardians",
        queryset=get_user_model().objects.filter(groups__name="Teachers"),
        many=True,
        label="Teachers",
    )
    url = serializers.HyperlinkedIdentityField(
        read_only=True, view_name="kids-detail"
    )
    pee_or_poos = PeeOrPooSerializer(many=True, read_only=True)

    class Meta:
        model = Kid
        exclude = ["guardians"]
