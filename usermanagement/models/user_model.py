from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(username=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    # Custom create_superuser
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    # Remove username field if using email as login
    phone = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager() 

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []  

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"


    def save(self, *args, **kwargs):
        print("Custom save called")
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def clean(self):
        if self.phone and not self.phone.isdigit():
            raise ValueError("Phone must be digits only")

    def set_password(self, raw_password):
        print("Custom set_password")
        return super().set_password(raw_password)







