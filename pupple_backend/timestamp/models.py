
from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    userdog = models.CharField(max_length=10)
    day = models.IntegerField(blank=True,null=True)
    press_time = models.CharField(max_length=8, blank=True, null=True)
    elapsed_time = models.IntegerField(blank=True,null=True)
    evaluate = models.BooleanField(blank=True,default=False,null=True)
    
    class Meta:
        db_table = 'timestamp_auth'
    
    def __str__(self):
        return self.press_time
