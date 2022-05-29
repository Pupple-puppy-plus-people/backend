from django.db import models
from users.models import User
from dogs.models import Dog

# Create your models here.
class TimeStamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timestamp")
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="timestamp")
    
    day = models.IntegerField(blank=True,null=True)
    press_time = models.CharField(max_length=8, blank=True, null=True)
    start_time = models.IntegerField(blank=True,null=True) 
    evaluate = models.BooleanField(blank=True,default=False,null=True)
   
    class Meta:
        db_table = 'timestamp_auth'
    
    def __str__(self):
        return self.dog + self.user + self.press_time
