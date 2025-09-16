from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from accounts.models import User
from accounts.serializers import UserSerializer,UserRegisterSerializer,CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class=UserRegisterSerializer
    permission_classes=[permissions.AllowAny]
    queryset=User.objects.all()

    

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=UserSerializer 

    def get_object(self):
        return self.request.user

