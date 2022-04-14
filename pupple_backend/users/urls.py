
from django.urls import path,include

from .views import registration_view # 추가
app_name = "users"

urlpatterns = [
    path('auth/register/', registration_view, name='register_user'),

]