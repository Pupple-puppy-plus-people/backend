
from django.contrib.auth.hashers import check_password
from django.shortcuts import render

# Create your views here.

from rest_framework.parsers import JSONParser

from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from dogs.models import Dog
from .serializers import RegistrationUserSerializer, LoginUserSerializer, WishListSerializer, WishListSerializer2
# from .models import Profile
from .models import User, Wishlist


# POST 로 데이터를 받을 것임을 명시해준다.
@api_view(['POST', ])
# 토큰이 없으면 페이지를 못들어온다. 때문에, 이 페이지에 관해서
# 권한을 다르게 설정해준다.
@permission_classes((permissions.AllowAny,))
def registration_view(request):
    # 요청의 메써드가 POST이면,
    if request.method == 'POST':

        # serializer를 불러와 request.data 를 집어넣는다.
        serializer = RegistrationUserSerializer(data=request.data)

        # 응답으로 보내줄 data의 초기화
        data = {}

        # serializer가 data 맛을 보고 이게 옳다 싶으면
        # .is_valid()를 True로 뱉는다.
        if serializer.is_valid():

            # serializer.save()를 거치면 저장을 한다.
            account = serializer.save()

            # 그치만, 저장이 됐는지를 응답을 해줘야 하므로 아래와 같이 응답데이터를 구성해준다.
            data['response'] = "successfully registred a new user"
            data['email'] = account.email
            data['username'] = account.username
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            data['user_type'] = account.user_type
            data['address'] = account.address

        else:
            data = serializer.errors
        return Response("ok")

# POST 로 데이터를 받을 것임을 명시해준다.
@api_view(['POST', ])
# 토큰이 없으면 페이지를 못들어온다. 때문에, 이 페이지에 관해서
# 권한을 다르게 설정해준다.
@permission_classes((permissions.AllowAny,))
def login_view(request):
    # 요청의 메써드가 POST이면,
    if request.method == 'POST':

        # serializer를 불러와 request.data 를 집어넣는다.
        serializer = LoginUserSerializer(data=request.data)

        # 응답으로 보내줄 data의 초기화
        data = {}

        # serializer가 data 맛을 보고 이게 옳다 싶으면
        # .is_valid()를 True로 뱉는다.
        # if serializer.is_valid():

        # serializer.save()를 거치면 저장을 한다.
        email = serializer.email
        pw = serializer.password
        try:
            user = User.objects.get(email=email)
            if check_password(pw, user.password):
                data['response'] = "successfully registred a new user"
                data['email'] = user.email
                data['username'] = user.username
                # token = Token.objects.get(user=account).key
                # data['token'] = token
                data['address'] = user.address
                data['id'] = user.id
                data['user_type'] = user.user_type
            else:
                data['error'] = "fail"

        except:
            data['error'] = "fail"

        # else:
        #     data = serializer.errors
        return Response(data)

@api_view(['POST',])
@permission_classes([permissions.AllowAny,])
def wishlistAdd_view(request):
    if request.method == 'POST':
        serializer = WishListSerializer(data=request.data)
        data = {}

        # serializer가 data 맛을 보고 이게 옳다 싶으면


        # serializer.save()를 거치면 저장을 한다.
        obj = serializer.save()

        # # 그치만, 저장이 됐는지를 응답을 해줘야 하므로 아래와 같이 응답데이터를 구성해준다.
        # data['response'] = "successfully registred a new user"
        # data['email'] = account1.email
        # data['dog_id'] = account2.id
        # # token = Token.objects.get(user=account).key
        # # data['token'] = token
        # data['user_type'] = account1.user_type
        # data['address'] = account1.address

        checker = Wishlist.objects.all()
        # print("adding obj = ",obj)
        # print("checker = ",checker)
        return Response(obj)

@api_view(['POST',])
@permission_classes([permissions.AllowAny,])
def wishlistDel_view(request):
    if request.method == 'POST':
        serializer = WishListSerializer(data=request.data)
        #data = {}
        deleteobj = serializer.delete()
        # print(deleteobj)
        return Response("ok")

@api_view(['POST', ])
@permission_classes([permissions.AllowAny, ])
def getAllWish_view(request):
    if request.method == 'POST':

        queryset = Wishlist.objects.all()
        # email 말고 dog_id도 받으려고 추가 하다보니 변경됨 -> 여쭤보기! 
        try:
            user = User.objects.get(email=request.data['email'])
            queryset = queryset.filter(user=user)
        except KeyError:
            pass
        
        try:
            dog_id = request.data['dog_id']
            queryset = queryset.filter(dog_id=dog_id)
        except KeyError:
            pass

        serializer_class = WishListSerializer2(queryset, many=True)
        print(serializer_class)
        # serializer_class = WishListSerializer2(obj)

       # return Response(obj_json)
        return Response(serializer_class.data)

@api_view(['POST',])
@permission_classes([permissions.AllowAny,])
def deleteAllWish_view(request):
    if request.method == 'POST':
        Wishlist.objects.all().delete()
        return Response("delete all")
    
@api_view(['POST',])
@permission_classes([permissions.AllowAny,])
def updateProgress_view(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.data['email'])
        dog = Dog.objects.get(id=request.data['dog_id'])
        obj = Wishlist.objects.get(user=user,dog_id=dog)
        
        total = 0
        
        if 'template1' in request.data:
            weight_count = request.data['my_count_total']/request.data['pass_count']
            weight_time = request.data['my_time_total']/(request.data['pass_time']*request.data['my_count_total'])
            weight_distance = request.data['my_distance_total']/(request.data['pass_distance']*request.data['my_count_total'])
            print('count weight :   ',weight_count)
            print('time weight :   ',weight_time)
            print('distance weight :   ',weight_distance)
            newProgress = (weight_count+weight_time+weight_distance)/3
            if newProgress > 1:
                newProgress = 100
            else:
                newProgress = newProgress * 100
            print('newProgress :   ',newProgress)
            
            Wishlist.objects.filter(user=user,dog_id=dog).update(template1 = newProgress)
            if dog.floor_auth and dog.house_auth:
                total = (newProgress + obj.template2 + obj.template3 + obj.template4) // 4
            elif dog.floor_auth or dog.house_auth:
                total = (newProgress + obj.template2 + obj.template3 + obj.template4) // 3
            else:
                total = (newProgress + obj.template2 + obj.template3 + obj.template4) // 2
            Wishlist.objects.filter(user=user,dog_id=dog).update(total = total)
        elif 'template2' in request.data:
            newProgress = int(request.data['template2'],base=10)
            Wishlist.objects.filter(user=user,dog_id=dog).update(template2 = newProgress)
            if dog.floor_auth and dog.house_auth:
                total = (obj.template1 + newProgress + obj.template3 + obj.template4) // 4
            elif dog.floor_auth or dog.house_auth:
                total = (obj.template1 + newProgress + obj.template3 + obj.template4) // 3
            else:
                total = (obj.template1 + newProgress + obj.template3 + obj.template4) // 2
            Wishlist.objects.filter(user=user,dog_id=dog).update(total = total)
        elif 'template3' in request.data:
            newProgress = int(request.data['template3'],base=10)
            Wishlist.objects.filter(user=user,dog_id=dog).update(template3 = newProgress)
            if dog.floor_auth and dog.house_auth:
                total = (obj.template1 + obj.template2 + newProgress + obj.template4) // 4
            elif dog.floor_auth or dog.house_auth:
                total = (obj.template1 + obj.template2 + newProgress + obj.template4) // 3
            else:
                total = (obj.template1 + obj.template2 + newProgress + obj.template4) // 2
            Wishlist.objects.filter(user=user,dog_id=dog).update(total = total)
        elif 'template4' in request.data:
            newProgress = int(request.data['template4'],base=10)
            Wishlist.objects.filter(user=user,dog_id=dog).update(template4 = newProgress)
            if dog.floor_auth and dog.house_auth:
                total = (obj.template1 + obj.template2 + obj.template3 + newProgress) // 4
            elif dog.floor_auth or dog.house_auth:
                total = (obj.template1 + obj.template2 + obj.template3 + newProgress) // 3
            else:
                total = (obj.template1 + obj.template2 + obj.template3 + newProgress) // 2
            Wishlist.objects.filter(user=user,dog_id=dog).update(total = total)
        return Response(newProgress)
    
