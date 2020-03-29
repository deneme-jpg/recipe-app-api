from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """creates and saves new user"""
        if not email:
            raise ValueError('Users must have an email adress')
        user = self.model(email=email.lower(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        if not password:
            raise ValueError('SuperUser must have password')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom User model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
