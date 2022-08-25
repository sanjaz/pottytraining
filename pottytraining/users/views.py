from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from pottytraining.users.serializers import (
    CreateUserSerializer,
    UserSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Admins")


class TeacherViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Teachers")


class ParentViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Parents")


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer
