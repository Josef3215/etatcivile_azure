from django.contrib.auth.models import AbstractUser
from django.db import models


class Emploie(AbstractUser):
    commune = models.CharField(max_length=50, blank=True)


# Create your models here.
