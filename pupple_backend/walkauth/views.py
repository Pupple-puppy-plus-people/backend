import math
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WalkAuthSerializer
from .models import WalkAuth

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.

class WalkAuthViewSet(viewsets.ModelViewSet):
    queryset = WalkAuth.objects.all()
    serializer_class = WalkAuthSerializer
    
    def get_queryset(self):
        queryset = WalkAuth.objects.all()
        userdog = self.kwargs['userdog']
        return queryset.filter(userdog=userdog).order_by('day')
        # 구매자와 강아지 아이디를 통해 pk인 userdog 사용

@api_view(['POST',])
@permission_classes([permissions.AllowAny,])
def updateWalkData_view(request):
    if request.method == 'POST':
        # need userdog, day, elapsed_time, distance
        timeCalculate = request.data['elapsed_time']
        timeCalculate = timeCalculate//60
        WalkAuth.objects.filter(userdog=request.data['userdog'],day=request.data['day']).update(distance=request.data['distance'],elapsed_time=timeCalculate)
        return Response("update success")
        
