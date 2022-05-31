import base64
import io
import os
from sys import api_version
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

import torch
import torchvision
from torchvision import transforms, datasets, models
from dogs.models import Dog

from users.models import User, Wishlist
from .serializers import MatDetectorSerializer,ResultMatDetectorSerializer
from PIL import Image

from .models import MatDetector
from .frcnn_model import get_model_instance_segmentation
# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def evaluateFloor_view(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.data['user_name'])
        dog = Dog.objects.get(id = request.data['dog_id'])
        
        serializer = MatDetectorSerializer(data=request.data)
        obj = serializer.save()
        
        # model create
        model = get_model_instance_segmentation(3)
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu') 
        model.to(device)
        # load model parameter
        # model.load_state_dict(torch.load('matDetectModel.pt'))
        model.load_state_dict(torch.load('/Users/errasi/capstone2022-1/backend/pupple_backend/mat_detector/matDetectModel.pt'))
                
        # start evaluate
        model.eval()
        data_transform = transforms.Compose([  # transforms.Compose : list 내의 작업을 연달아 할 수 있게 호출하는 클래스
        transforms.ToTensor() # ToTensor : numpy 이미지에서 torch 이미지로 변경
        ])
        
        # convert base64 to Image data type
        sliceBase64 = request.data['image']
        img2data = base64.b64decode(sliceBase64[1:len(sliceBase64)-1])
        dataBytesIO = io.BytesIO(img2data)
        image = Image.open(dataBytesIO).convert("RGB")
        
        gotoModel = data_transform(image)
        tensorList = [gotoModel]
        bestScore=0
        pred = model(tensorList)
        for id in range(len(pred)):
            idx_list=[]
            for idx, score in enumerate(pred[id]['scores']):
                if score > 0.5:
                    idx_list.append(idx)

            pred[id]['boxes'] = pred[id]['boxes'][idx_list]
            pred[id]['labels'] = pred[id]['labels'][idx_list]
            pred[id]['scores'] = pred[id]['scores'][idx_list]

            if idx_list.__len__() > 0:
                if bestScore < max(pred[id]['scores']):
                    bestScore = max(pred[id]['scores'])
                
        newProgress = 0
        total = 0
        wishlistObj = Wishlist.objects.get(user=user,dog_id=dog)
        if bestScore > 0.5:
            serializer.evaluate(True)
            newProgress = 100
            Wishlist.objects.filter(user=user,dog_id=dog).update(template4 = newProgress)
            if dog.floor_auth and dog.house_auth:
                total = (wishlistObj.template1 + wishlistObj.template2 + wishlistObj.template3 + newProgress) // 4
            elif dog.floor_auth or dog.house_auth:
                total = (wishlistObj.template1 + wishlistObj.template2 + wishlistObj.template3 + newProgress) // 3
            else:
                total = (wishlistObj.template1 + wishlistObj.template2 + wishlistObj.template3 + newProgress) // 2
            Wishlist.objects.filter(user=user,dog_id=dog).update(total = total)
        else:
            serializer.evaluate(False)
            newProgress = 0
            Wishlist.objects.filter(user=user,dog_id=dog).update(template4 = newProgress)
            if dog.floor_auth and dog.house_auth:
                total = (wishlistObj.template1 + wishlistObj.template2 + wishlistObj.template3 + newProgress) // 4
            elif dog.floor_auth or dog.house_auth:
                total = (wishlistObj.template1 + wishlistObj.template2 + wishlistObj.template3 + newProgress) // 3
            else:
                total = (wishlistObj.template1 + wishlistObj.template2 + wishlistObj.template3 + newProgress) // 2
            Wishlist.objects.filter(user=user,dog_id=dog).update(total = total)
        
        obj = serializer.save()
        return Response(obj)
    
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def getIimage_view(request):
    if request.method == 'POST':
        user_name = request.data['user_name']
        dog_id = request.data['dog_id']
        
        obj = MatDetector.objects.get(user_name=user_name,dog_id=dog_id)
        serializer_class = ResultMatDetectorSerializer(obj)
        
        return Response(serializer_class.data)