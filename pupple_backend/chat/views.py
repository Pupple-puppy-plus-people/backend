from email import message
from django.utils.safestring import mark_safe
import json
from asgiref.sync import sync_to_async
from time import sleep

# Create your views here.

from rest_framework.parsers import JSONParser

from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Chat
from .serializers import ChatSerializer
from django.http import HttpResponse


def index(request):
    print("index ok")
    return

def room(request, room_name):
    print("room ok")
    return  mark_safe(json.dumps(room_name))

  
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_chat_messages_view(request):

    
    #payload = {}
    #payload['messages'] = messages
    #field_object = Chat._meta.get_field('message')
    
    #for message in messages:
    #    field_value = field_object.value_from_object(message)
    #    message_history.append(field_value)

    if request.method == 'POST':
        sleep(0.001)
    
        room_number = request.data['room_number']
        message_history = Chat.objects.filter(room_number=room_number).order_by('-timestamp')
                
        serializer_class = ChatSerializer(message_history, many=True)

        return Response(serializer_class.data)
    

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_unread_chat_check_view(request):
    data = {}
    if request.method == 'POST':
        #serializer = DogSerializer(data=request.data)
        room_number = request.data['room_number']
        user_type = request.data['user_type']
       
        messages = Chat.objects.filter(room_number=room_number).order_by('timestamp')

        if user_type == 'customer':
            messages = messages.filter(user_type='seller', received=False)
        if user_type == 'seller':
            messages = messages.filter(user_type='customer', received=False)
        
        print("messages", messages, room_number, user_type)
        if messages.exists():
            data['unread'] = "true"
            print("true")
            return Response(data)

        data['unread'] = "false"
        print("false")

        return Response(data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def update_unread_chat_to_read_view(request): # 안 읽은 메시지를 읽음 처리 해줌
    data = {}
    if request.method == 'POST':
        #serializer = DogSerializer(data=request.data)
        room_number = request.data['room_number']
        user_type = request.data['user_type']

        messages = Chat.objects.filter(room_number=room_number)
        if user_type == 'customer':
            messages = messages.filter(user_type='seller', received=False)
        if user_type == 'seller':
            messages = messages.filter(user_type='customer', received=False)
        
        if messages.exists():
            messages.update(received=True)
            print("UPDATED")

        data['response'] = "success"
        return Response(data)


