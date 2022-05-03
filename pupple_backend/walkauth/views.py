from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WalkAuthSerializer
from .models import WalkAuth

import time
# Create your views here.

class WalkAuthViewSet(viewsets.ModelViewSet):
    queryset = WalkAuth.objects.all()
    serializer_class = WalkAuthSerializer
    
    def get_queryset(self):
        queryset = WalkAuth.objects.all()
        userdog = self.kwargs['userdog']
        return queryset.filter(userdog=userdog).order_by('day')
        # 구매자와 강아지 아이디를 통해 query 구성

    

