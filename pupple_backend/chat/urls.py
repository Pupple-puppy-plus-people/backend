from django.conf.urls import url
from . import consumers

urlpatterns = [
        url('ws/chat/<room_name>/', consumers.ChatConsumer),
]