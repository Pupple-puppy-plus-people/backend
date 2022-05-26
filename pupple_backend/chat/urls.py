
from django.urls import path,include

from .views import get_chat_messages_view, update_unread_chat_to_read_view, get_unread_chat_check_view
app_name = "chat"

urlpatterns = [
        #path('', views.index, name='index'),
        path('history/', get_chat_messages_view, name='get_chat_messages'),
        path('update/', update_unread_chat_to_read_view, name='update_unread_chat_to_read'),
        path('check/', get_unread_chat_check_view, name='update_unread_chat_to_read'),
]