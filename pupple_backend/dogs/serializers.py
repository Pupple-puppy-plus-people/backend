from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = (
            'id',
            'registration_number',
            'image',
            'name',
            'gender',
            'kind',
            'desexing',
            'age',
            'location',
            'size',
            'hair_loss',
            'bark_term',
            'activity',
            'person_personality',
            'adoptation_status',
            'introduction',
            'approval',
            'user_id',
            'house_auth',
            'floor_auth',
        )

class DogSerializer2(serializers.Serializer):
    
    def __init__(self, data):
        self.registration_number = data['registration_number']
        self.image = data['image'][0]
        self.name=data['name']
        self.gender=data['gender']
        self.kind=data['kind']
        self.desexing=data['desexing']
        self.age=data['age']
        self.location=data['location']
        self.size=data['size']
        self.hair_loss=data['hair_loss']
        self.bark_term=data['bark_term']
        self.activity=data['activity']
        self.person_personality=data['person_personality']
        self.adoptation_status=data['adoptation_status'],
        self.introduction=data['introduction']
        self.approval=data['approval']
        self.user_id=data['user_id']
        self.house_auth=data['house_auth']
        self.floor_auth=data['floor_auth']         

    def save(self):
        data = {}
        try:
            #self.image
            dog = Dog(
                registration_number = self.registration_number,
                image = self.image,
                name = self.name,
                gender = self.gender,
                kind = self.kind,
                desexing = self.desexing,
                age = self.age,
                location = self.location,
                size = self.size,
                hair_loss = self.hair_loss,
                bark_term = self.bark_term,
                activity = self.activity,
                person_personality = self.person_personality,
                adoptation_status = self.adoptation_status,
                introduction = self.introduction,
                approval = self.approval,
                user_id = self.user_id,
                house_auth = self.house_auth,
                floor_auth = self.floor_auth
            )
            dog.save()
            latest_id = Dog.objects.latest('id').id
            print("latest_id", latest_id)
            data['pk'] = latest_id

        except Exception as e:
            print(e)
            data['error']="fail"

        return data
