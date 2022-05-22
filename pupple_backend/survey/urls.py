from django.urls import path,include, re_path
from rest_framework import routers
from . import views
from .views import update_survey_view, getsurvey_view, del_survey_view, update_agreement_view, get_agreement_view

app_name = "survey"
urlpatterns = [
    path('survey/update',update_survey_view,name='update_survey'),
    path('survey/delete',del_survey_view,name='del_survey'),
    path('survey/get',getsurvey_view,name='get_survey'),
    path('agreement/update',update_agreement_view,name='update_agreement'),
    path('agreement/get',get_agreement_view,name='get_agreement'),
    #path('agreement/',updatephoto_view,name='get_housephoto'),
]