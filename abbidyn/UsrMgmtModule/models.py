# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    address = models.TextField(blank=False)

    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '9999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    pincode_regex = RegexValidator(regex=r'^\d{6}$',)
    pincode = models.IntegerField(validators=[pincode_regex],blank=True, default=500000)

    is_cook = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.email
