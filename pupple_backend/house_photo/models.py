from django.db import models
from users.models import User
from dogs.models import Dog
# Create your models here.
class HousePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="housephoto")
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="housephoto")
    photo = models.TextField()
    ispass = models.BooleanField(default=False)
    username = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.user.email