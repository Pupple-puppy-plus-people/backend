from django.urls import path,include
from rest_framework import routers
from . import views

app_name = 'pass_condition'

router = routers.DefaultRouter()
router.register(r'',views.PassConditionViewSet)

urlpatterns = [
    path('',include(router.urls))
]
