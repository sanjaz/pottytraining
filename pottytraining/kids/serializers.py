from django.contrib.auth import get_user_model
from rest_framework import serializers

from pottytraining.kids.models import Kid


class KidSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(
        source="guardians",
        queryset=get_user_model().objects.filter(groups__name="Teachers"),
        many=True,
        label="Teachers",
    )

    class Meta:
        model = Kid
        exclude = ["guardians"]
