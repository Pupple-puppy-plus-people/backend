from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
from .serializers import HousePhotoSerializer,SendHousePhotoSerializer
from .models import HousePhoto
from dogs.models import Dog
from users.models import User, Wishlist


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
            serializer_class = SendHousePhotoSerializer(obj, many=True)
        
        return Response(serializer_class.data)


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def update_house_photo_pass(request):
    if request.method == 'POST':
        dog_obj = Dog.objects.get(id=request.data['dog_id'])
        user_obj = User.objects.get(id=request.data['user_id'])
        did_pass = request.data['pass'] # pass면 True로, fail이면 False로
        data={}
        try:
            print("tryyy")
            housephoto_obj = HousePhoto.objects.get(user=user_obj,dog=dog_obj)
            print("housephoto_obj ", housephoto_obj)
            if not housephoto_obj.ispass : # false일때만 True로 업데이트
                HousePhoto.objects.filter(user=user_obj,dog=dog_obj).update(ispass=did_pass)

                if did_pass:
                    print("did_pass : ", did_pass)
                    wishlist_obj = Wishlist.objects.get(user=user_obj, dog_id=dog_obj)
                    # print("wishlist_obj : ", wishlist_obj.total)
                    newProgress = 100
                    Wishlist.objects.filter(user=user_obj,dog_id=dog_obj).update(template3 = newProgress)
                    if dog_obj.floor_auth and dog_obj.house_auth:
                        total = (wishlist_obj.template1 + wishlist_obj.template2 + newProgress + wishlist_obj.template4) // 4
                    elif dog_obj.floor_auth or dog_obj.house_auth:
                        total = (wishlist_obj.template1 + wishlist_obj.template2 + newProgress + wishlist_obj.template4) // 3
                    else:
                        total = (wishlist_obj.template1 + wishlist_obj.template2 + newProgress + wishlist_obj.template4) // 2
                    Wishlist.objects.filter(user=user_obj,dog_id=dog_obj).update(total = total)
                    print("update house photo and get updated object: ",Wishlist.objects.get(user=user_obj,dog_id=dog_obj))
                data['request'] = "success"

            else:
                data['request'] = "already full"
        except:
            data['error'] = "fail"


        return Response(data)
