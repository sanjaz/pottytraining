from django_filters import rest_framework as filters
from django.contrib.auth.models import User


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='iexact')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    role = filters.CharFilter(
        lookup_expr='iexact',
        label='Role',
        field_name='groups__name'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role']
