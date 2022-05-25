from django.utils.safestring import mark_safe
import json

def index(request):
    print("index ok")
    return

def room(request, room_name):
    print("room ok")
    return  mark_safe(json.dumps(room_name))

