from ast import walk
from django.contrib import admin

# Register your models here.
from .models import TimeStamp
admin.site.register(TimeStamp)