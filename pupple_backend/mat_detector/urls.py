from django.urls import path
from . import views
app_name = 'mat_detector'
urlpatterns = [
    path('evaluate/',views.evaluateFloor_view,name='evaluateFloor_view'),
    path('getimage/',views.getIimage_view,name='getImage_view'),
]
