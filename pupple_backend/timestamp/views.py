from tracemalloc import start
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TimeStampSerializer, TimeStampSerializer2
from .models import TimeStamp
from rest_framework.response import Response

from dogs.models import Dog
from users.models import User
import time

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

class TimeStampViewSet(viewsets.ModelViewSet):
    queryset = TimeStamp.objects.all()
    serializer_class = TimeStampSerializer

    def get_queryset(self):
        queryset = TimeStamp.objects.all()

        user = self.request.GET.get('user',None)
        dog = self.request.GET.get('dog',None)
        day = self.request.GET.get('day',None)
        press_time = self.request.GET.get('press_time',None)
        start_time = self.request.GET.get('start_time',None)
        evaluate = self.request.GET.get('evaluate',None)
        try:
            if queryset.exists():
                if user:
                    queryset = queryset.filter(user=user)
                if dog:
                    queryset = queryset.filter(dog=dog)
                if day:
                    queryset = queryset.filter(day=day)
                if press_time:
                    queryset = queryset.filter(press_time=press_time)
                if start_time:
                    queryset = queryset.filter(start_time=start_time)
                if evaluate:
                    queryset = queryset.filter(evaluate=evaluate)
            else:
                print("HIHHI")
        except Exception as e:
            print("HIHHI1")
            print(e)
        return queryset


@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def updateTimestamp_view(request):
    if request.method == 'POST':
        serializer = TimeStampSerializer2(data=request.data)
        obj = serializer.save()
        return Response(obj)


'''
def getAllphoto_view(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.data['email'])
        dog_obj = Dog.objects.filter(user=user)
        obj = HousePhoto.objects.filter(dog=dog_obj)
        serializer_class = HousePhotoSerializer(obj, many=True)

        return Response(serializer_class)
'''