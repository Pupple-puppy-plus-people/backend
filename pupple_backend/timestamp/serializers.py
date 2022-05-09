from rest_framework import serializers
from .models import TimeStamp

class TimeStampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeStamp
        fields = (
            'id',
            'userdog',
            'day',
            'press_time',
            'elapsed_time',
            'evaluate',
        )
