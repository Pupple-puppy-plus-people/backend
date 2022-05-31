from dataclasses import fields
from email.mime import image
from unittest import result
from rest_framework import serializers

from house_photo.models import HousePhoto
from .models import MatDetector

class MatDetectorSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    dog_id = serializers.CharField()
    image = serializers.CharField()
    result = serializers.CharField()
    
    def __init__(self, data):
        if 'user_name' in data:
            self.user_name = data['user_name']
        if 'dog_id' in data:
            self.dog_id = data['dog_id']
        if 'image' in data:
            self.image = data['image']
        self.result = 'inProgress'
    
    def save(self):
        data = {}
        try:
            user_name = self.user_name
            dog_id = self.dog_id
            if MatDetector.objects.filter(user_name=user_name,dog_id=dog_id).exists():
                MatDetector.objects.filter(user_name=user_name,dog_id=dog_id).update(image=self.image)
            else:
                matdetector = MatDetector(
                    user_name = user_name,
                    dog_id = dog_id,
                    image = self.image,
                    result = 'inProgress'
                )
                matdetector.save()
            data['learning_result']=self.result
            data['response']='success'
        except:
            data['response']='fail'
        return data
    
    def evaluate(self,detected):
        if detected == True:
            MatDetector.objects.filter(user_name=self.user_name,dog_id=self.dog_id).update(result='detected')
            self.result = 'detected'
        else:
            MatDetector.objects.filter(user_name=self.user_name,dog_id=self.dog_id).update(result='undetected')
            self.result = 'undetected'
        
class ResultMatDetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatDetector
        fields=(
            'user_name',
            'dog_id',
            'image',
            'result',
        )