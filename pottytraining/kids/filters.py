from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

from pottytraining.kids.models import Kid


class KidFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr="iexact")
    last_name = filters.CharFilter(lookup_expr="iexact")
    teacher = filters.ModelChoiceFilter(
        queryset=get_user_model().objects.filter(groups__name="Teachers"),
        label="Teacher",
        field_name="guardians",
    )

    class Meta:
        model = Kid
        fields = ["first_name", "last_name", "gender", "teacher"]


class TeacherKidFilter(KidFilter):
    teacher = filters.ModelChoiceFilter(
        queryset=get_user_model().objects.filter(groups__name="Teachers"),
        label="Teacher",
        field_name="guardians",
        method="filter_teachers",
    )

    def filter_teachers(self, queryset, name, value):
        return queryset.filter(guardians=self.request.user)
