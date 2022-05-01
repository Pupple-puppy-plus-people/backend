from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=False, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class User(AbstractUser):
    user_type = models.CharField(max_length=50, default='customer')
    address = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.username


