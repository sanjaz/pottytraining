from django.contrib.auth.models import Group, User
from rest_framework import serializers


# Define the API representation of User.
class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), many=True
    )

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "first_name",
            "last_name",
            "groups",
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), many=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "groups",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        groups = validated_data.pop("groups")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        for group in groups:
            user.groups.add(group)
        return user
