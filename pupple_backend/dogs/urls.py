from django.urls import path,include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.DogViewSet)

urlpatterns = [
    path('list/',include(router.urls)),
    path('add/',views.updatephoto_view),
]
