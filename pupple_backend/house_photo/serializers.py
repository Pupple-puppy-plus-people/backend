from csv import excel
from rest_framework import serializers
from .models import HousePhoto
from users.models import User
from dogs.models import Dog


class HousePhotoSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    dog_id = serializers.IntegerField()
    image = serializers.CharField()

    def __init__(self, data):
        if 'email' in data:
            self.email = data['email']
        if 'dog_id' in data:
            self.dog_id = data['dog_id']
        if 'image' in data:
            self.image = data['image']
        # print(self.email, " ",self.dog_id," ",self.image)

    def save(self):
        data = {}
        try:
            user = User.objects.get(email=self.email)
            dog = Dog.objects.get(id=self.dog_id)
            #print("여기까지는되는거???",user.email," ",dog.id)
            if HousePhoto.objects.filter(user=user, dog=dog).exists():
                HousePhoto.objects.filter(user=user, dog=dog).update(photo=self.image)
                data['response'] = "success"
                data['status'] = "update"
            else:

                #print("여기까지는되는거22222???",self.image)
                housephoto = HousePhoto(
                    user=user,
                    dog=dog,
                    photo=self.image,
                    ispass=False,
                    username=user.username
                )
                #print("여기까지는되는거333333???", housephoto)
                housephoto.save()
                #print("여기까지는되는거333333???")
                data['response'] = "success"
                data['status'] = "create"
        except:
            data['error']="fail"

        return data

class SendHousePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePhoto
        exclude = ('id',)
        # fields = (
        #     'photo',
        #     'ispass',
        #     'user',
        #     'dog',
        #     'username',
        # )

