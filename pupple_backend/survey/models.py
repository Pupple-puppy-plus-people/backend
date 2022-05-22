from django.db import models
from users.models import User
from dogs.models import Dog

# Create your models here.
class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="survey")
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="survey")
    reason = models.TextField()
    num_family = models.IntegerField()
    family = models.TextField()
    family_agree = models.BooleanField()
    experience = models.BooleanField()
    house_form = models.CharField(max_length=100)
    noise_issue = models.TextField()
    move_issue = models.TextField()
    empty_issue = models.TextField()
    family_issue = models.TextField()
    neutering = models.BooleanField()
    main_person = models.TextField()
    vaccin_cost = models.TextField()
    food_cost = models.TextField()

    def __str__(self):
        return self.user.email + " " + self.dog.name


class Agreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agreement")
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="agreement")
    person_info = models.BooleanField(null=True,default=False)
    location_info = models.BooleanField(null=True,default=False)
    chit_penalty = models.BooleanField(null=True,default=False)
    cannot_adopt = models.BooleanField(null=True,default=False)
    more_info = models.BooleanField(null=True,default=False)

    def __str__(self):
        return self.user.email + " " + self.dog.name
