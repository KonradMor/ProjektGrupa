from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_boss = models.BooleanField()

    def __str__(self):
        return self.user.username
