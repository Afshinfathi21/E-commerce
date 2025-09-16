from django.shortcuts import render
from rest_framework import viewsets,permissions,response
from .serializers import Inventory,InventorySerializer
from rest_framework.exceptions import PermissionDenied
# Create your views here.

class InventoryView(viewsets.ModelViewSet):
    serializer_class=InventorySerializer
    queryset=Inventory.objects.all()

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        user=self.request.user

        if not getattr(user,'is_staff',False):
            raise PermissionDenied('Detail:Only admin can modify inventory.')
        serializer.save()
