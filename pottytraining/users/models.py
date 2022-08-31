from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def is_admin(self):
        return self.groups.filter(name='Admins').exists()
