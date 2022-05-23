from rest_framework import serializers
from .models import Survey, Agreement
from users.models import User
from dogs.models import Dog

class SurveySerializer(serializers.Serializer):
    user_id = serializers.StringRelatedField()
    dog_id = serializers.StringRelatedField()
    reason = serializers.CharField()
    num_family = serializers.IntegerField()
    family = serializers.CharField()
    family_agree = serializers.BooleanField()
    experience = serializers.BooleanField()
    house_form = serializers.CharField()
    noise_issue = serializers.CharField()
    move_issue = serializers.CharField()
    empty_issue = serializers.CharField()
    family_issue = serializers.CharField()
    neutering = serializers.BooleanField()
    main_person = serializers.CharField()
    vaccin_cost = serializers.CharField()
    food_cost = serializers.CharField()

    def __init__(self,data):
        self.user_id = data['user_id']
        self.dog_id = data['dog_id']
        self.reason = data['reason']
        self.num_family = data['num_family']
        self.family = data['family']
        self.family_agree = data['family_agree']

        self.experience = data['experience']
        self.house_form = data['house_form']
        self.noise_issue = data['noise_issue']
        self.move_issue = data['move_issue']
        self.empty_issue = data['empty_issue']
        self.family_issue = data['family_issue']
        self.neutering = data['neutering']
        self.main_person = data['main_person']
        self.vaccin_cost = data['vaccin_cost']
        self.food_cost = data['food_cost']




    def save(self):
        data = {}
        try:
            # print("try sentence")
            user = User.objects.get(id=self.user_id)
            dog = Dog.objects.get(id=self.dog_id)
            # print("user = ",user,"   dog = ",dog)

            if Survey.objects.filter(user=user, dog=dog).exists():
                Survey.objects.filter(user=user, dog=dog).update(
                    reason=self.reason,
                    num_family=self.num_family,
                    family=self.family,
                    family_agree=self.family_agree,
                    experience=self.experience,
                    house_form=self.house_form,
                    noise_issue=self.noise_issue,
                    move_issue=self.move_issue,
                    empty_issue=self.empty_issue,
                    family_issue=self.family_issue,
                    neutering=self.neutering,
                    main_person=self.main_person,
                    vaccin_cost=self.vaccin_cost,
                    food_cost=self.food_cost,
                )
            else:
                survey = Survey(
                    user=user,
                    dog=dog,
                    reason=self.reason,
                    num_family=self.num_family,
                    family=self.family,
                    family_agree=self.family_agree,
                    experience=self.experience,
                    house_form=self.house_form,
                    noise_issue=self.noise_issue,
                    move_issue=self.move_issue,
                    empty_issue=self.empty_issue,
                    family_issue=self.family_issue,
                    neutering=self.neutering,
                    main_person=self.main_person,
                    vaccin_cost=self.vaccin_cost,
                    food_cost=self.food_cost,
                )
                survey.save()
            data['response'] = "success"
        except:
            data['error'] = "fail"

        return data


class AgreementSerializer(serializers.Serializer):
    user_id = serializers.StringRelatedField()
    dog_id = serializers.StringRelatedField()
    person_info = serializers.BooleanField()
    location_info = serializers.BooleanField()
    chit_penalty = serializers.BooleanField()
    cannot_adopt = serializers.BooleanField()
    more_info = serializers.BooleanField()

    def __init__(self,data):
        self.user_id = data['user_id']
        self.dog_id = data['dog_id']
        self.person_info = data['person_info']
        self.location_info = data['location_info']
        self.chit_penalty = data['chit_penalty']
        self.cannot_adopt = data['cannot_adopt']

        self.more_info = data['more_info']


    def save(self):
        data = {}
        try:
            # print("try sentence")
            user = User.objects.get(id=self.user_id)
            dog = Dog.objects.get(id=self.dog_id)
            # print("user = ",user,"   dog = ",dog)

            if Agreement.objects.filter(user=user, dog=dog).exists():
                Agreement.objects.filter(user=user, dog=dog).update(
                    person_info=self.person_info,
                location_info = self.location_info,
                chit_penalty = self.chit_penalty,
                cannot_adopt = self.cannot_adopt,
                more_info = self.more_info,
                )
            else:
                agreement = Agreement(
                    user=user,
                    dog=dog,
                    person_info=self.person_info,
                    location_info=self.location_info,
                    chit_penalty=self.chit_penalty,
                    cannot_adopt=self.cannot_adopt,
                    more_info=self.more_info,
                )
                agreement.save()
            data['response'] = "success"
        except:
            data['error'] = "fail"

        return data


