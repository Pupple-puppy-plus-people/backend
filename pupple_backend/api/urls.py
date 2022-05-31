from django.urls import path,include
from rest_framework import routers
from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('example/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dogs/',include('dogs.urls')),
    path('walkauth/',include('walkauth.urls')),
    path('timestamp/',include('timestamp.urls')),

    #path('createdog/',include('dogs.urls')), dogs/create
    #path('wishlist/',include('wishlist.urls')),
    #path('test/',include('test.urls')),
    path('users/',include('users.urls')),
    path('housephoto/',include('house_photo.urls')),
    path('passcondition/',include('pass_condition.urls')),
    path('survey/',include('survey.urls')),
    path('matdetector/',include('mat_detector.urls')),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('chat/',include('chat.urls')), # r은 정규표현식, ^는 정규표현식 시작
]