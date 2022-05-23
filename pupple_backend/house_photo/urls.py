from django.urls import path,include, re_path
from rest_framework import routers
from . import views
from .views import get_dog_customer_matched_photo_view, updatephoto_view, getphoto_view, get_all_mydog_photo_view,get_one_dog_photo_view
app_name = "housephoto"
urlpatterns = [
    path('add/',updatephoto_view,name='register_housephoto'),
    path('get/',getphoto_view,name='get_housephoto'),
    path('get/mydog/',get_all_mydog_photo_view,name='get_all_mydog_photo_view'), # 판매자 email만 입력받으면 판매자가 가진 모든 강아지에게 온 사진데이터 전송
    path('get/mydog/onlyone/',get_one_dog_photo_view,name='get_one_dog_photo_view'), # 강아지 아이디를 입력 받으면 해당 강아지아이디로 온 모든 사진데이터 전송
    path('get/evaluate/',get_dog_customer_matched_photo_view,name='get_dog_customer_matched_photo_view'),
]