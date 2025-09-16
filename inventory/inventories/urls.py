from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import InventoryView


router=DefaultRouter()
router.register(r'inventory',InventoryView,basename='inventory')

urlpatterns = [
    path('',include(router.urls))
]
