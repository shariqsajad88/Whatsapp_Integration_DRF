<<<<<<< HEAD

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
=======
from django.db import models

# Create your models here.
>>>>>>> 47943c7aebd196923dca4de5fb234ee7a12f87eb
