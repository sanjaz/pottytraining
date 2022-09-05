from django.contrib.auth import get_user_model
from rest_framework import serializers

from pottytraining.kids.models import Kid, PeeOrPoo


class PeeOrPooSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeeOrPoo
        fields = ["id", "is_poo", "time", "note"]


class KidSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(
        source="guardians",
        queryset=get_user_model().objects.filter(groups__name="Teachers"),
        many=True,
        label="Teachers",
    )
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='kids-detail'
    )
    pee_or_poos = PeeOrPooSerializer(many=True, read_only=True)

    class Meta:
        model = Kid
        exclude = ["guardians"]



