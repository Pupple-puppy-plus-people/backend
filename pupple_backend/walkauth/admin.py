from ast import walk
from django.contrib import admin

# Register your models here.
from .models import WalkAuth
admin.site.register(WalkAuth)