
from django.db import models

# Create your models here.
class WalkAuth(models.Model):
    userdog = models.CharField(max_length=10)
    day = models.IntegerField(blank=True,null=True)
    start_time = models.IntegerField(blank=True,null=True)
    elapsed_time = models.IntegerField(blank=True,null=True)
    end_time = models.IntegerField(blank=True,null=True)
    distance = models.IntegerField(blank=True,null=True)
    evaluate = models.BooleanField(blank=True,default=False,null=True)
    
    class Meta:
        db_table = 'walk_auth'
    
    def __str__(self):
        return self.userdog
        # return self.user_name