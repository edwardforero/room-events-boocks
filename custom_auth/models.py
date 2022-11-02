from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator


class UserManager(BaseUserManager):
    

    def create_user(self, email, password=None, **extra_args):
        if email is None:
            raise TypeError("Email is required")
        if password is None:
            raise TypeError("Password is required")
        normalized_email = self.normalize_email(email)
        user = self.model(email=normalized_email, **extra_args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_args):
        user = self.create_user(email, password, **extra_args)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    BUSINESS = 'BU'
    CUSTOMER = 'CU'
    USER_ROLES = [
        (BUSINESS, 'Business'),
        (CUSTOMER, 'Customer'),
    ]
    
    username = None
    email = models.EmailField(max_length= 150, unique=True, db_index=True)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(6)])
    role = models.CharField(
        max_length=2,
        choices=USER_ROLES,
        # default=CUSTOMER,
        error_messages={"invalid_choice": "Please select: BU for Bussines and CU for Customer"},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('role', 'password')
    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    def tokens(self):
        return ''
        