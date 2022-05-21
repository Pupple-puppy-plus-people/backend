from tkinter import image_names
from rest_framework import viewsets
from .serializers import DogSerializer
from .models import Dog
# Create your views here.

from datetime import datetime
from django.utils.text import slugify
from photologue.models import Photo

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from django.shortcuts import render 
from rest_framework import status 
from django.http.response import HttpResponse 
from rest_framework.decorators import action


class DogViewSet(viewsets.ModelViewSet):
    # queryset = Dog.objects.all().order_by('id')
    queryset = Dog.objects.all().order_by('id')
    serializer_class = DogSerializer
    
    def get_queryset(self):
        queryset = Dog.objects.all()
        
        #id = self.request.GET.get('id',None)
        gender = self.request.GET.get('gender',None)
        kind = self.request.GET.get('kind',None)
        desexing = self.request.GET.get('desexing',None)
        age = self.request.GET.get('age',None)
        size = self.request.GET.get('size',None)
        hair_loss = self.request.GET.get('hair_loss',None)
        bark_term = self.request.GET.get('bark_term',None)
        activity = self.request.GET.get('activity',None)
        person_personality = self.request.GET.get('person_personality',None)
        user_id = self.request.GET.get('user_id',None)
 
        #if id:
        #    queryset = queryset.filter(id=id)
        if gender:
            queryset = queryset.filter(gender=gender)
        if kind:
            queryset = queryset.filter(kind=kind)
        if desexing:
            queryset = queryset.filter(desexing=desexing)
        if age:
            queryset = queryset.filter(age=age)
        if size:
            queryset = queryset.filter(size=size)
        if hair_loss:
            queryset = queryset.filter(hair_loss=hair_loss)
        if bark_term:
            queryset = queryset.filter(bark_term=bark_term)
        if activity:
            queryset = queryset.filter(activity=activity)
        if person_personality:
            queryset = queryset.filter(person_personality=person_personality)
        if user_id:
            queryset = queryset.filter(user_id=user_id)   

        return queryset.order_by('id')


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updatephoto_view(request):
    print("Here")
    def create_photo(image):
        title = f'{datetime.now()}'
        slug = slugify(title)
        photo = Photo.objects.create(
            title=title,
            slug=slug,
            image=image,
        )
        return photo

    if request.method == 'POST':
        #serializer = DogSerializer(data=request.data)
        #obj = serializer.save()
        #image = request.POST.get(image=request.data['image'])
        print("LOG raw image :: ")
        #obj = create_photo(image)
        #print("LOG url image :: ", obj)
        return Response("hello")
