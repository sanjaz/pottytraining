from django.contrib.auth import get_user_model
from rest_framework import serializers

from pottytraining.kids.models import Kid


class KidSerializer(serializers.ModelSerializer):
    guardians = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.filter(groups__name="Teachers"),
        many=True,
        label="Teachers"
    )

    class Meta:
        model = Kid
        fields = '__all__'