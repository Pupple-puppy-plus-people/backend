from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TimeStampSerializer
from .models import TimeStamp

import time
# Create your views here.

class TimeStampViewSet(viewsets.ModelViewSet):
    queryset = TimeStamp.objects.all().order_by('id')
    serializer_class = TimeStampSerializer

'''   
    def get_queryset(self):
        queryset = TimeStamp.objects.all()
        
        userdog = self.request.GET.get('userdog',None)
        day = self.request.GET.get('day',None)
        press_time = self.request.GET.get('press_time',None)
        elapsed_time = self.request.GET.get('elapsed_time',None)
        evaluate = self.request.GET.get('evaluate',None)

          
        if userdog:
            queryset = queryset.filter(userdog=userdog)
        if day:
            queryset = queryset.filter(day=day)
        if evaluate:
            queryset = queryset.filter(evaluate=evaluate)
        
        return queryset.order_by('id')
'''