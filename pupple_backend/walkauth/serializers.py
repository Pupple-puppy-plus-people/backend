from rest_framework import serializers
from .models import WalkAuth

class WalkAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WalkAuth
        fields = (
            'id',
            'start_time',
            'elapsed_time',
            'distance',
        )