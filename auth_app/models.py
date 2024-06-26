from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from auth_app import manager
# Create your models here.

class UserModel(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = None
    email = models.EmailField(unique=True,)
    date_of_birth = models.DateField(blank=True, null=True)

    objects = manager.UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()
