from re import T
from django.db import models

# Create your models here.
class WalkAuth(models.Model):
    start_time = models.IntegerField(blank=True,null=True)
    elapsed_time = models.IntegerField(blank=True,null=True)
    distance = models.IntegerField(blank=True,null=True)
    
    class Meta:
        db_table = 'walk_auth'
    
    def __str__(self):
        return self.start_time
        # return self.user_name