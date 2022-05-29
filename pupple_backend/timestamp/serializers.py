from rest_framework import serializers
from .models import TimeStamp
from users.models import User
from dogs.models import Dog

class TimeStampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeStamp
        fields = (
            'user',
            'dog',
            'day',
            'press_time',
            'start_time',
            'evaluate',
        )

class TimeStampSerializer2(serializers.Serializer):
    user = serializers.IntegerField()
    dog = serializers.IntegerField()
    day = serializers.IntegerField()
    press_time = serializers.CharField()
    start_time = serializers.IntegerField()
    evaluate = serializers.BooleanField()
   
    def __init__(self, data):
        if 'user' in data:
            self.user = data['user']
        if 'dog' in data:
            self.dog = data['dog']
        if 'day' in data:
            self.day = data['day']
        if 'press_time' in data:
            self.press_time = data['press_time']
        if 'start_time' in data:
            self.start_time = data['start_time']
        if 'evaluate' in data:
            self.evaluate = data['evaluate']
          
    def save(self):
        data = {}
        try:
            print("SUCCEED1", self)

            user = User.objects.get(id=self.user)
            dog = Dog.objects.get(id=self.dog)
            
            timestamp = TimeStamp(
                user=user,
                dog=dog,
                day=self.day,
                press_time=self.press_time,
                start_time=self.start_time,
                evaluate=self.evaluate,
            )
            print("SUCCEED2", data)

            #print("여기까지는되는거333333???", housephoto)
            timestamp.save()
            #print("여기까지는되는거333333???")
            data['response'] = "success"
            data['status'] = "create"
            print("SUCCEED2", data)

        except:
            data['error']="fail"

        print("SUCCEED", data)
        return data
