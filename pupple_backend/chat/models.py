from django.db import models

from users.models import User
from dogs.models import Dog

from django.utils import timezone

# Create your models here.
class Chat(models.Model):
    
    # 채팅방 번호
    room_number = models.CharField(max_length=50)
    # 메시지
    message = models.TextField()
    # 보낸 메시지 읽었는지 
    received = models.BooleanField(default=False)
    # 강아지 
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="chat")
    # 구매자
    customer = models.IntegerField()
    # 판매자
    seller = models.IntegerField()
    # 메시지 시간
    timestamp = models.DateTimeField(default=timezone.now) #만들어진 시간


    class Meta:
        db_table = 'chat'

    def __str__(self):
        return self.room_number
