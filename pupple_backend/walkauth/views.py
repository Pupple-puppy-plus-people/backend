from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WalkAuthSerializer
from .models import WalkAuth

import time
# Create your views here.

class WalkAuthViewSet(viewsets.ModelViewSet):
    queryset = WalkAuth.objects.all().order_by('id')
    serializer_class = WalkAuthSerializer
