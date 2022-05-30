from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import SurveySerializer, AgreementSerializer
from .models import Survey, Agreement
from users.models import User
from dogs.models import Dog
# from rest_framework import viewsets
# Create your views here.

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def update_survey_view(request):
    if request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        data = serializer.save()
        return Response(data)


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def getsurvey_view(request):
    if request.method == 'POST':
        # print("get_survey")
        user = User.objects.get(id=request.data['user_id'])
        dog = Dog.objects.get(id=request.data['dog_id'])
        survey = Survey.objects.get(user=user,dog=dog)
        # print(survey)
        data={}
        data['user_name']=survey.user.username
        data['response']="success"
        data['reason']=survey.reason
        data['family'] = survey.family
        data['num_family'] = survey.num_family
        data['family_agree'] = survey.family_agree
        data['experience'] = survey.experience
        data['house_form'] = survey.house_form
        data['noise_issue'] = survey.noise_issue
        data['move_issue'] = survey.move_issue
        data['empty_issue'] = survey.empty_issue
        data['family_issue'] = survey.family_issue
        data['neutering'] = survey.neutering
        data['main_person'] = survey.main_person
        data['vaccin_cost'] = survey.vaccin_cost
        data['food_cost'] = survey.food_cost
        # data = serializer.save()
        return Response(data)


@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def del_survey_view(request):
    if request.method == 'POST':
        Survey.objects.all().delete()

        return Response("ok")

@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def update_agreement_view(request):
    if request.method == 'POST':
        serializer = AgreementSerializer(data=request.data)
        data = serializer.save()
        return Response(data)


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def get_agreement_view(request):
    if request.method == 'POST':
        # print("get_survey")
        user = User.objects.get(id=request.data['user_id'])
        dog = Dog.objects.get(id=request.data['dog_id'])
        agreement = Agreement.objects.get(user=user,dog=dog)

        data={}
        data['user_name']=agreement.user.username
        data['response']="success"
        data['person_info']=agreement.person_info
        data['location_info'] = agreement.location_info
        data['chit_penalty'] = agreement.chit_penalty
        data['cannot_adopt'] = agreement.cannot_adopt
        data['more_info'] = agreement.more_info
        data['dog_entrance'] = agreement.dog_entrance
        # data = serializer.save()
        return Response(data)