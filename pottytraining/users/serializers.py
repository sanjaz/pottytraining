from django.contrib.auth.models import User
from rest_framework import serializers


# Define the API representation of User.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = User
        fields = [
            'url', 'username', 'email', 'first_name', 'last_name', 'groups'
        ]
