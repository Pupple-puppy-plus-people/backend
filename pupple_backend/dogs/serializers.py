from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = (
            'id',
            'registration_number',
            'image',
            'name',
            'gender',
            'kind',
            'desexing',
            'age',
            'location',
            'size',
            'hair_loss',
            'bark_term',
            'activity',
            'person_personality',
            'adoptation_status',
            'introduction',
            'approval',
            'user_id',
            'house_auth',
            'floor_auth',
        )