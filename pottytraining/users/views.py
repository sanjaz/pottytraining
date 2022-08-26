from django.contrib.auth.models import Group, User
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets

from pottytraining.users.filters import UserFilter
from pottytraining.users.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
    group_name = None

    serializers = {
        "default": UserSerializer,
        "create": CreateUserSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])

    def perform_create(self, serializer):
        if self.group_name is None:
            serializer.save()
        else:
            # TODO: validate group name
            user = serializer.save()
            group = Group.objects.get(name=self.group_name)
            group.user_set.add(user)


class AdminViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Admins")
    group_name = "Admins"


class TeacherViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Teachers")
    group_name = "Teachers"


class ParentViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Parents")
    group_name = "Parents"


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
