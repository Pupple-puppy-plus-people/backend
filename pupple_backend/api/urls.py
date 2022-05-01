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
]