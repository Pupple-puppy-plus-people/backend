from django.urls import path,include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.DogViewSet)
# router.register(r'add', views.DogViewSet)
app_name='dogs'

urlpatterns = [
    path('list/',include(router.urls)),
    path('add/',views.updatedog_view),
]

#path('add/',views.updatephoto_view,name='post_dogphoto'),
    # path('add/',views.DogViewSet.updatephoto_view),
