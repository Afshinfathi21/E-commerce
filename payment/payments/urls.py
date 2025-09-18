from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PaymentView

router=DefaultRouter()
router.register(r'payment',PaymentView,basename='payment')

urlpatterns = [
    path('',include(router.urls))
]
