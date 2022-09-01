from django.conf import settings
from django.db import models


class Gender(models.IntegerChoices):
    UNKNOWN = 0, "Not known"
    MALE = 1, "Male"
    FEMALE = 2, "Female"


class Kid(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=Gender.choices)
    birth_date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    guardians = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['last_name', 'first_name']
