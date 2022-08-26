from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets

from pottytraining.users.filters import UserFilter
from pottytraining.users.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
    group_name = None
    queryset = get_user_model().objects.none()

    serializers = {
        "default": UserSerializer,
        "create": CreateUserSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])

    def get_queryset(self):
        if self.group_name is None:
            return get_user_model().objects.all()
        else:
            return get_user_model().objects.filter(
                groups__name=self.group_name
            )

    def perform_create(self, serializer):
        if self.group_name is None:
            serializer.save()
        else:
            # TODO: validate group name
            user = serializer.save()
            group = Group.objects.get(name=self.group_name)
            group.user_set.add(user)


class AdminViewSet(UserViewSet):
    group_name = "Admins"


class TeacherViewSet(UserViewSet):
    group_name = "Teachers"


class ParentViewSet(UserViewSet):
    group_name = "Parents"


class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CreateUserSerializer
