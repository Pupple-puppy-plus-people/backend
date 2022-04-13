from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DogSerializer
from .models import Dog
# Create your views here.

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all().order_by('id')
    serializer_class = DogSerializer