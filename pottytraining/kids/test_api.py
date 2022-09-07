from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from pottytraining.kids.models import Gender, Kid, PeeOrPoo

user_model = get_user_model()


def list_kids_url() -> str:
    return reverse("kids-list")


def create_kid_url() -> str:
    return reverse("kids-create")


def detail_kid_url(id) -> str:
    return reverse("kids-detail", args=[id])


def get_sample_kid_data() -> dict:
    return {
        "first_name": "Jelena",
        "last_name": "Jovanovic",
        "gender": Gender.FEMALE,
    }


def create_and_get_kid() -> Kid:
    data = get_sample_kid_data()
    return Kid.objects.create(**data)


def list_pee_or_poos_url(kid_id) -> str:
    return reverse("pee_or_poos-list", args=[kid_id])


def create_pee_or_poo_url(kid_id) -> str:
    return reverse("pee_or_poos-create", args=[kid_id])


def detail_pee_or_poo_url(kid_id, id) -> str:
    return reverse("pee_or_poos-detail", args=[kid_id, id])


def get_sample_pee_or_poo_data(kid) -> dict:
    return {
        "time": timezone.now(),
        "kid": kid,
        "is_poo": "False",
        "note": "Sve u nosu.",
    }


def create_and_get_pee_or_poo(kid) -> PeeOrPoo:
    data = get_sample_pee_or_poo_data(kid=kid)
    return PeeOrPoo.objects.create(**data)


def set_kid_teacher(kid, teacher):
    kid.guardians.add(teacher)


def get_user_in_group(group_name):
    user = user_model.objects.create_user(username="test", password="pwd")
    group = Group.objects.get_or_create(name=group_name)[0]
    user.groups.add(group)
    user.save()
    return user


def get_admin_user():
    return get_user_in_group(group_name="Admins")


def get_teacher_user():
    return get_user_in_group(group_name="Teachers")


class KidsApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def log_in_as_admin(self):
        """Logs in as an admin."""
        admin_user = get_admin_user()
        self.client.force_login(admin_user)

    def log_in_as_teacher(self):
        """Logs in as a teacher."""
        teacher = get_teacher_user()
        self.client.force_login(teacher)

    def test_list_kids(self):
        self.log_in_as_admin()
        res = self.client.get(list_kids_url())
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_kids_no_permissions(self):
        res = self.client.get(list_kids_url())
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_kid(self):
        self.log_in_as_teacher()
        res = self.client.post(create_kid_url(), get_sample_kid_data())
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_kid(self):
        self.log_in_as_admin()
        kid = create_and_get_kid()
        data_to_update = {"last_name": "Mitic"}
        url = detail_kid_url(kid.id)
        res = self.client.patch(url, data_to_update)
        kid.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(kid.last_name, data_to_update["last_name"])

    def test_delete_kid(self):
        self.log_in_as_admin()
        kid = create_and_get_kid()
        url = detail_kid_url(kid.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Kid.objects.filter(id=kid.id).exists())

    def test_kid_details(self):
        self.log_in_as_admin()
        kid = create_and_get_kid()
        url = detail_kid_url(kid.id)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class PeeOrPooApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.kid = create_and_get_kid()

    def log_in_as_teacher(self):
        """Logs in as a teacher."""
        teacher = get_teacher_user()
        self.client.force_login(teacher)
        return teacher

    def test_list_pee_or_poos(self):
        self.log_in_as_teacher()
        res = self.client.get(list_pee_or_poos_url(kid_id=self.kid.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_kids_no_permissions(self):
        res = self.client.get(list_pee_or_poos_url(kid_id=self.kid.id))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_pee_or_poo(self):
        self.log_in_as_teacher()
        res = self.client.post(
            create_pee_or_poo_url(kid_id=self.kid.id),
            get_sample_pee_or_poo_data(kid=self.kid),
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_pee_or_poo(self):
        teacher = self.log_in_as_teacher()
        set_kid_teacher(kid=self.kid, teacher=teacher)
        pee_or_poo = create_and_get_pee_or_poo(kid=self.kid)
        data_to_update = {"is_poo": True}
        url = detail_pee_or_poo_url(kid_id=self.kid.id, id=pee_or_poo.id)
        res = self.client.patch(url, data_to_update)
        pee_or_poo.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(pee_or_poo.is_poo, data_to_update["is_poo"])

    def test_delete_pee_or_poo(self):
        teacher = self.log_in_as_teacher()
        set_kid_teacher(self.kid, teacher)
        pee_or_poo = create_and_get_pee_or_poo(kid=self.kid)
        url = detail_pee_or_poo_url(kid_id=self.kid.id, id=pee_or_poo.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(PeeOrPoo.objects.filter(id=pee_or_poo.id).exists())

    def test_pee_or_poo_details(self):
        teacher = self.log_in_as_teacher()
        set_kid_teacher(self.kid, teacher)
        pee_or_poo = create_and_get_pee_or_poo(kid=self.kid)
        url = detail_pee_or_poo_url(kid_id=self.kid.id, id=pee_or_poo.id)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
