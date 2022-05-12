from xml.etree.ElementTree import tostring
from django.db import models

# Create your models here.
class PassCondition(models.Model):
    dog_id = models.IntegerField(primary_key=True)
    walk_total_count = models.IntegerField(blank=True,null=True)
    min_per_walk = models.IntegerField(blank=True,null=True)
    meter_per_walk = models.IntegerField(blank=True,null=True)
    ts_total_count = models.IntegerField(blank=True,null=True)	
    ts_check_time = models.IntegerField(blank=True,null=True)
    
    class Meta:
        db_table = 'pass_condition'
    
    def __str__(self):
        return str(self.dog_id)