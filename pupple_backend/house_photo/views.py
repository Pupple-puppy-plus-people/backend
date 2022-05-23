from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
from .serializers import HousePhotoSerializer,SendHousePhotoSerializer
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
        dog = Dog.objects.get(id=request.data['dog_id'])
        user = User.objects.get(email=request.data['email'])

        obj = HousePhoto.objects.get(user=user,dog=dog)
        serializer_class = SendHousePhotoSerializer(obj)

        return Response(serializer_class.data)

@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def get_all_mydog_photo_view(request):
    if request.method == 'POST':
        # 강아지 주인 이메일
        user = User.objects.get(email=request.data['email'])
        # 강아지 주인이 입양 보내려 하는 강아지들
        dog_obj = Dog.objects.filter(user_id=user.id)
        # print("dog : ", dog_obj)
        obj = []
        for d in dog_obj:
            # print(d)
            if HousePhoto.objects.filter(dog=d).exists():
                # print("housephoto : ", HousePhoto.objects.filter(dog=d))

                obj += HousePhoto.objects.filter(dog=d)
        # obj = HousePhoto.objects.filter(dog=dog_obj, many=True)
        # print("obj : ",obj)
        serializer_class = SendHousePhotoSerializer(obj, many=True)
        # print("data[0] : ",serializer_class.data[0])
        return Response(serializer_class.data)

@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def get_one_dog_photo_view(request):
    if request.method == 'POST':
        # 입양 보내려 하는 강아지 한마리
        dog_obj = Dog.objects.get(id=request.data['dog_id'])
        # print("dog : ", dog_obj)
        obj = []
        # print(dog_obj)
        if HousePhoto.objects.filter(dog=dog_obj).exists():
            # print("housephoto : ", HousePhoto.objects.filter(dog=dog_obj))

            obj += HousePhoto.objects.filter(dog=dog_obj)
        # obj = HousePhoto.objects.filter(dog=dog_obj, many=True)
        # print("obj : ",obj)
        serializer_class = SendHousePhotoSerializer(obj, many=True)
        # print("data[0] : ",serializer_class.data[0])
        return Response(serializer_class.data)
    
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def get_dog_customer_matched_photo_view(request):
    if request.method == 'POST':
        dog_obj = Dog.objects.get(id=request.data['dog_id'])
        user_obj = User.objects.get(id=request.data['user_id'])
        serializer_class=SendHousePhotoSerializer()
        
        if HousePhoto.objects.filter(dog=dog_obj).filter(user=user_obj).exists():
            obj = HousePhoto.objects.filter(dog=dog_obj).filter(user=user_obj)
            serializer_class = SendHousePhotoSerializer(obj,many=True)
        
        return Response(serializer_class.data)