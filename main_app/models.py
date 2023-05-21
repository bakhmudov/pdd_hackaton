from django.db import models
from django.contrib.auth.models import User, Permission, Group
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now=timezone.now)
    amount = models.IntegerField(blank=True, null=True)
    decision = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Appeal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set'
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customgroups_set'
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)
