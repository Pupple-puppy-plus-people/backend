# chat/routing.py

from django.conf.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # r은 정규식 표현임을 알려주는 표시
    # as_asgi(): 각각의 연결에 consumer의 인스턴스 생성을 위해 클래스 메서드를 사용한다. 
    # re_path: 내부 라우터가 미들웨어에 감싸져있을 경우 path() 함수는 제대로 동작하지 않을수 있기 때문에 사용
    re_path(r'ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]