from django.urls import path,include, re_path
from rest_framework import routers
from . import views
from .views import updatephoto_view, getphoto_view, getAllphoto_view
app_name = "housephoto"
urlpatterns = [
    path('add/',updatephoto_view,name='register_housephoto'),
    path('get/',updatephoto_view,name='get_housephoto'),
    path('get/mydog/',updatephoto_view,name='get_mydog_housephoto'),
]