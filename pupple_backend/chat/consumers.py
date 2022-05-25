import json
from channels.generic.websocket import AsyncWebsocketConsumer

from channels.db import database_sync_to_async
from .models import Chat

class ChatConsumer(AsyncWebsocketConsumer):
    
    # websocket 연결 시 실행
    async def connect(self):
        print("connected!")

        # routing.py에 있는 url에서 room_name 가져옴 - AuthMiddlewareStack가 scope에 kwargs 형태로 채워준 것을 꺼내서 사용?
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # channle_layer는 두가지 개념이 있는데 1) channel(채팅 참여자 역할) 2) group(채팅방 역할)
        self.room_group_name = 'chat_%s' % self.room_name
        # group에 channel추가
        await (self.channel_layer.group_add)( # async_to_sync : 동기적인 send를 비동기적으로 사용하기 위해
            self.room_group_name, # 그룹명
            self.channel_name # 채널명: 자동으로 uniqu하게 생성됨
        )
        await self.accept()


    # websocket 연결 종료 시 실행
    async def disconnect(self, close_code):
         # group에서 제거 --> 다음 단계) 대화 내용이 남는 단톡방을 만들고 싶은데 
        await (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # 클라이언트로부터 메세지를 받을 시 실행
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        #print("annggg?", text_data_json)
        message = text_data_json

        print("message :", message) 
        #create_room_chat_message(self.scope['url_route']['kwargs']['room_name'], message)

        # 클라이언트로부터 받은 메세지를 다시 클라이언트로 보내준다.
        await (self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_channel_name': self.channel_name
            }
        )

    # group 에서 메세지 receive
    async def chat_message(self, event):
        message = event['message']

        # 보낸 사람 제외 상대방 WebSocket 에게 메세지 전송
        if self.channel_name != event['sender_channel_name']:
            await self.send(text_data=json.dumps({
                'message': message
            }))


@database_sync_to_async
def create_room_chat_message(room_number, message): # 메시지 저장
    
    room_info = room_number.split(".")
    dog = room_info[0]
    customer = room_info[1]
    seller = room_info[2]
    return Chat.objects.create(room_number=room_number, message=message, dog=dog, customer=customer, seller=seller)

'''
@database_sync_to_async
def get_chat_messages(room, page_number): # 메시지 출력
	try:
		qs = Chat.objects.by_room(room)
		p = Paginator(qs, DEFAULT_ROOM_CHAT_MESSAGE_PAGE_SIZE)

		payload = {}
		messages_data = None
		new_page_number = int(page_number)  
		if new_page_number <= p.num_pages:
			new_page_number = new_page_number + 1
			s = LazyRoomChatMessageEncoder()
			payload['messages'] = s.serialize(p.page(page_number).object_list)
		else:
			payload['messages'] = "None"
		payload['new_page_number'] = new_page_number
		return json.dumps(payload)
	except Exception as e:
		print("EXCEPTION: " + str(e))
	return None
'''