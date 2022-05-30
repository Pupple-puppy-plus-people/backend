from rest_framework import serializers
from .models import TimeStamp
from users.models import User
from dogs.models import Dog

class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        exclude = ('id',)



class TimeStampSerializer2(serializers.Serializer):
    
    def __init__(self, data):
        #print(self, data)

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
            timestamp.save()
            data['response'] = "success"
            data['status'] = "create"

        except Exception as e:
            print(e)
            data['error']="fail"

        return data
