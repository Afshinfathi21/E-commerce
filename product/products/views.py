from rest_framework import viewsets,filters,permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer


# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['category','price']
    search_fields=['name']
    ordering_fields=['price','name','created_at']


    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            #i should check requested user is authenticated or not by sending request to user service.
            permission_classes=[permissions.IsAuthenticated]
            return [permission() for permission in permission_classes]
        return [permissions.AllowAny()]
