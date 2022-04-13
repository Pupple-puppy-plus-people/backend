
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
# from .serializers import UserSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# Create your views here.
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer