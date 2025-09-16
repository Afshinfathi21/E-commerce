from django.urls import path
from .views import RegisterView,ProfileView,CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('login/',CustomTokenObtainPairView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
]
