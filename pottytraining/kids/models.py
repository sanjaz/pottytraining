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
        ordering = ["last_name", "first_name"]

    @property
    def full_name(self) -> str:
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self) -> str:
        return self.full_name


class PeeOrPoo(models.Model):
    is_poo = models.BooleanField()
    kid = models.ForeignKey(
        Kid, on_delete=models.CASCADE, related_name="pee_or_poos"
    )
    time = models.DateTimeField()
    note = models.TextField(blank=True)

    class Meta:
        ordering = ["kid__id", "time"]
