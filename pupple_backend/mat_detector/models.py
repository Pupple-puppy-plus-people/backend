from django.db import models

# Create your models here.
class MatDetector(models.Model):
    user_name = models.TextField(blank=True,null=True)
    dog_id = models.TextField(blank=True,null=True)
    image = models.TextField(blank=True,null=True)
    result = models.TextField(default='inProgress')
    
    class Meta:
        db_table = 'mat_detector'
        
    def __str__(self):
        return self.user_name