from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
from .serializers import HousePhotoSerializer
from .models import HousePhoto
from dogs.models import Dog
from users.models import User


@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def updatephoto_view(request):
    if request.method == 'POST':
        serializer = HousePhotoSerializer(data=request.data)
        obj = serializer.save()
        return Response(obj)


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def getphoto_view(request):
    if request.method == 'POST':
        dog = Dog.objects.get(dog=request.data['dog_id'])

        obj = HousePhoto.objects.filter(dog=dog)
        serializer_class = HousePhotoSerializer(obj, many=True)

        return Response(serializer_class)

def getAllphoto_view(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.data['email'])
        dog_obj = Dog.objects.filter(user=user)
        obj = HousePhoto.objects.filter(dog=dog_obj)
        serializer_class = HousePhotoSerializer(obj, many=True)

        return Response(serializer_class)