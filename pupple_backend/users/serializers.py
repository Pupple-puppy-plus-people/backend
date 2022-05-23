from rest_framework import serializers
from .models import User, Wishlist
from dogs.models import Dog


# from .models import Profile



class RegistrationUserSerializer(serializers.ModelSerializer):

    class Meta:
        """
        메타 클래스에 필드, 모델 등을 설정하고
        password 필드의 스타일을 정해준다.
        """
        model = User
        fields = ["username", "email","password","user_type","address"]


    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            user_type=self.validated_data['user_type'],
            address=self.validated_data['address'],
            password=self.validated_data['password']
        )
        user.set_password(self.validated_data['password'])
        # print(user)
        user.save()
        return user
    #     # exclude= ('id',)
    # # def __init__(self, data):
    # #     self.username = data.username
    # #     self.password = data.password
    # #     self.email = data.email
    # #     self.
    #
    # def save(self):
    #     """
    #     저장시 한 번 더 확인한다.
    #     """
    #     user = User(self.validated_data['username'], self.validated_data['email'])
    #     password = self.validated_data['password']
    #     user.set_password(password)
    #     user.save()
    #
    #     account = Profile()
    #     account.user = user
    #     account.user_type = self.validated_data['user_type']
    #     account.address = self.validated_data['address']
    #
    #
    #     # if password != password2:
    #     #     raise serializers.ValidationError({'password': 'Passwords must match'})
    #     # account.set_password(password)
    #     account.save()
    #     return account

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField()
    def __init__(self, data):
        self.email = data['email']
        self.password = data['password']


class WishListSerializer(serializers.Serializer):

    email = serializers.EmailField(read_only=True)
    dog_id = serializers.CharField()

    def __init__(self, data):
        self.email = data['email']
        if 'dog_id' in data:
            self.dog_id = data['dog_id']
        else:
            self.dog_id = 0

    def save(self):
        data = {}
        try:
            user = User.objects.get(email=self.email)
            dog = Dog.objects.get(id=self.dog_id)
            # print(Wishlist.objects.filter(user=user,dog_id=dog).exists())
            if Wishlist.objects.filter(user=user,dog_id=dog).exists():
                data['error'] = "fail"
                data['response'] = "duplicate"
                return data
            else:
                wishlist = Wishlist(
                    user=user,
                    dog_id=dog,
                )
                wishlist.save()
                data['response'] = "success"
                data['email'] = user.email
                data['dog_id'] = dog.id
        except:
            data['error'] = "fail"

        # print(user)

        return data

    def delete(self):
        user = User.objects.get(email=self.email)
        dog = Dog.objects.get(id=self.dog_id)
        wishlist = Wishlist.objects.get(user=user,dog_id=dog)
        wishlist.delete()
        return wishlist


class WishListSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        exclude = ('id',)


    def get(self):
        user = User.objects.get(email=self.email)
        wishlist = Wishlist.objects.get(user=user)
        data={}
        # print(wishlist)
        return wishlist
