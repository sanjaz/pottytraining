from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from pottytraining.kids.models import Gender, Kid


def list_kids_url() -> str:
    return reverse("kids-list")


def create_kid_url() -> str:
    return reverse("kids-create")


def detail_kid_url(id) -> str:
    return reverse("kids-detail", args=[id])


def get_sample_kid_data() -> str:
    return {
        "first_name": "Jelena",
        "last_name": "Jovanovic",
        "gender": Gender.FEMALE,
    }


def create_and_get_kid() -> Kid:
    data = get_sample_kid_data()
    return Kid.objects.create(**data)


class KidsApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_model = get_user_model()

    def get_admin_user(self):
        user = self.user_model.objects.get_or_create(username="test")[0]
        group = Group.objects.get_or_create(name="Admins")[0]
        user.groups.add(group)
        self.client.force_login(user)
        return user

    def log_in_as_admin(self):
        """Logs in as an admin."""
        admin_user = self.get_admin_user()
        self.client.force_login(admin_user)

    def test_list_kids(self):
        self.log_in_as_admin()
        res = self.client.get(list_kids_url())
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_kids_no_permissions(self):
        res = self.client.get(list_kids_url())
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_kid(self):
        self.log_in_as_admin()
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
