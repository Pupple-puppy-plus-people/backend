
from django.urls import path,include

from .views import registration_view, login_view, wishlistDel_view, wishlistAdd_view, deleteAllWish_view, \
    getAllWish_view  # 추가
app_name = "users"

urlpatterns = [
    path('auth/register/', registration_view, name='register_user'),
    path('auth/login/', login_view, name='login'),
    path('wishlist/add/', wishlistAdd_view, name='register_wishlist'),
    path('wishlist/delete/', wishlistDel_view, name='delete_wishlist'),
    path('wishlist/deleteall/', deleteAllWish_view, name='deleteAllWish'),
    path('wishlist/', getAllWish_view, name='getAllWish'),
]