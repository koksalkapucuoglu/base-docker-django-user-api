import uuid
import os
from django.db import models

# if we want to use extended user model, we must import following modules
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                            PermissionsMixin
from django.conf import settings



"""
Burada BaseUserManager'ın tüm özelliklerini kullanacağız fakat usernme yerine
email bekleyecek şekilde override edeceğiz
"""


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


"""
Benzer şekilde emaili destekleyecek şekilde diğer modülleri de override
etmeliyiz
"""


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"