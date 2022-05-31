# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# If you want make model which already exists,
# then type 'python manage.py inspector > (app name)/models.py' in command line
# This adds all models in the database set as the default DB in settings.py to (app name)/models.py.
class Dog(models.Model):
    registration_number = models.CharField(max_length=50, blank=True, null=True)

    image = models.TextField()
    #image = models.CharField('photologue.Photo',null=True,blank=True,on_delete=models.SET_NULL,)
    
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    kind = models.CharField(max_length=50, blank=True, null=True)
    desexing = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    hair_loss = models.CharField(max_length=50, blank=True, null=True)
    bark_term = models.CharField(max_length=50, blank=True, null=True)
    activity = models.CharField(max_length=50, blank=True, null=True)
    person_personality = models.CharField(max_length=50, blank=True, null=True)
    adoptation_status = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.CharField(max_length=1024, blank=True, null=True)
    approval = models.CharField(max_length=50, blank=True, null=True)

    user_id = models.CharField(max_length=50, blank=True, null=True)
    house_auth = models.BooleanField(blank=True,default=False,null=True)
    floor_auth = models.BooleanField(blank=True,default=False,null=True)

    class Meta:
        db_table = 'dog'

    def __str__(self):
        return self.name
