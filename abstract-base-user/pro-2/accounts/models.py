# ---Django---
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, phone_number, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            name=name, email=self.normalize_email(email), phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone_number, password=None):

        user = self.create_user(
            email=email, phone_number=phone_number, password=password
        )

        user.is_staff = True
        user.is_admin = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser):
    name = models.CharField(verbose_name="name", max_length=100)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name="phone number", unique=True, max_length=20
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone_number"]

    objects = UserProfileManager()
