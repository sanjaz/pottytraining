from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr="iexact")
    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")
    role = filters.CharFilter(
        lookup_expr="iexact", label="Role", field_name="groups__name"
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email", "role"]
