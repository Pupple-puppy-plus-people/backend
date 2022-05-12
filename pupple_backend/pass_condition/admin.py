from ast import Pass
from django.contrib import admin

# Register your models here.
from .models import PassCondition
admin.site.register(PassCondition)