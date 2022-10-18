from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

from core.models import TimeStampModel


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str = None) -> object:
        if not email:
            raise ValueError('EMAIL_IS_REQUIRED')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str = None) -> object:
        if not email:
            raise ValueError('EMAIL_IS_REQUIRED')

        superuser = self.create_user(email=email, password=password)

        superuser.is_staff = True
        superuser.is_superuser = True

        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin, TimeStampModel):
    email = models.EmailField(max_length=127, unique=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'User'