from rest_framework import serializers
from .models import PassCondition

class PassConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PassCondition
        fields = [
            'dog_id',
            'walk_total_count',
            'min_per_walk',
            'meter_per_walk',
            'ts_total_count',
            'ts_check_time'
        ]