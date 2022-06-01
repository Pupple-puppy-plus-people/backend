from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.WalkAuthViewSet)

urlpatterns = [
    path('<str:userdog>/info/',include(router.urls)),
    path('update/',views.updateWalkData_view,name='updateWalkData_view'),
]
