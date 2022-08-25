from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import permissions, status, viewsets
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


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_create(request):
    if request.method == 'POST':
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
