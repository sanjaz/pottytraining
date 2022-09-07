from django.test import TestCase
from django.utils import timezone

from pottytraining.kids import models


class KidModelTest(TestCase):
    def test_kid_model_full_name(self):
        kid = models.Kid.objects.create(
            first_name="Jelena",
            last_name="Jovanovic",
            gender=models.Gender.FEMALE,
        )
        self.assertEqual(kid.full_name, "Jelena Jovanovic")

    def test_kid_model_str(self):
        kid = models.Kid.objects.create(
            first_name="Jelena",
            last_name="Jovanovic",
            gender=models.Gender.FEMALE,
        )
        self.assertEqual(str(kid), kid.full_name)


class PeeOrPooModelTest(TestCase):
    def test_pee_or_poo_model_str(self):
        now = timezone.now()
        kid = models.Kid.objects.create(
            first_name="Jelena",
            last_name="Jovanovic",
            gender=models.Gender.FEMALE,
        )
        pee_or_poo = models.PeeOrPoo.objects.create(
            kid=kid, is_poo=False, time=now
        )
        self.assertEqual(str(pee_or_poo), "%s %s" % (str(kid), str(now)))
