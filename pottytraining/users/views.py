from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets

from pottytraining.users.filters import UserFilter
from pottytraining.users.permissions import IsAdmin
from pottytraining.users.serializers import (
    CreateUserSerializer,
    UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
    group_name = None
    queryset = get_user_model().objects.none()
    permission_classes = [IsAdmin]

    serializers = {
        "default": UserSerializer,
        "create": CreateUserSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])

    def get_serializer_context(self):
        context = super(UserViewSet, self).get_serializer_context()
        context.update({"group_name": self.group_name})
        return context

    def get_queryset(self):
        if self.group_name is None:
            return get_user_model().objects.all()
        else:
            return get_user_model().objects.filter(
                groups__name=self.group_name
            )


class AdminViewSet(UserViewSet):
    group_name = "Admins"


class TeacherViewSet(UserViewSet):
    group_name = "Teachers"


class ParentViewSet(UserViewSet):
    group_name = "Parents"


class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CreateUserSerializer
