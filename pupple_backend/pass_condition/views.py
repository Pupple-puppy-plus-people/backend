from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PassConditionSerializer
from .models import PassCondition
# Create your views here.

class PassConditionViewSet(viewsets.ModelViewSet):
    queryset = PassCondition.objects.all().order_by('dog_id')
    serializer_class = PassConditionSerializer
    
    def get_queryset(self):
        queryset = PassCondition.objects.all()
        dog_id = self.kwargs['dog_id']
        return queryset.filter(dog_id = dog_id)