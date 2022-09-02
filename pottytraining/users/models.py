from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def is_admin(self):
        return self.groups.filter(name="Admins").exists()

    def is_teacher(self):
        return self.groups.filter(name="Teachers").exists()

    def is_admin_or_teacher(self):
        return self.groups.filter(name__in=["Admins", "Teachers"]).exists()
