from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator
import uuid
from rest_framework_simplejwt.serializers import TokenObtainSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','phone']


class UserRegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    username=serializers.CharField(max_length=20,required=False)
    password1=serializers.CharField(max_length=20,write_only=True)
    password2=serializers.CharField(max_length=20,write_only=True)

    def validate(self, data):
        

        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords must be same.')
        

        return data
    def create(self, validated_data):
        if not validated_data.get('username'):
            random_suffix=uuid.uuid4().hex[:6]
            username=f'user_{random_suffix}'
        user=User.objects.create_user(email=validated_data.get('email'),username=username)
        user.set_password(validated_data.get('password1'))
        user.save()
        return user