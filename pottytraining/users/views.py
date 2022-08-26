from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from pottytraining.users.serializers import (
    CreateUserSerializer,
    UserSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializers = {
        'default': UserSerializer,
        'create': CreateUserSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(
            self.action,
            self.serializers['default']
        )


class AdminViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Admins")


class TeacherViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Teachers")


class ParentViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Parents")


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
