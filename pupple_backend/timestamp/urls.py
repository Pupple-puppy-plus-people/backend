from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.TimeStampViewSet)
app_name = "timestamp"

urlpatterns = [
    path('get/',include(router.urls)),
    path('add/',views.updateTimestamp_view,name='updateTimestamp'),
]
