from rest_framework import serializers
from .models import User
from .models import Profile



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

