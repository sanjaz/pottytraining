from django.contrib.auth.models import User
from rest_framework import viewsets

from pottytraining.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Admins")
    serializer_class = UserSerializer


class TeacherViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Teachers")
    serializer_class = UserSerializer


class ParentViewSet(UserViewSet):
    queryset = User.objects.filter(groups__name="Parents")
    serializer_class = UserSerializer
