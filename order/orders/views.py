from django.shortcuts import render
from rest_framework import permissions,viewsets,response,status
from .models import Order
from .serializers import OrderSerializer
from .utils import product_exist,check_inventory,reduce_inventory
from rest_framework.exceptions import NotFound
# Create your views here.

class OrderView(viewsets.ModelViewSet):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        user=self.request.user
        product_id=request.data.get('product')
        quantity=int(request.data.get('quantity'))
        token=self.request.headers.get('Authorization')
        if not product_exist(product_id):
            # raise NotFound('Product not exist in database,check again.')
            return response.Response('Detail:Product Not Found.',status=status.HTTP_404_NOT_FOUND)
        
        if not check_inventory(product_id,quantity):
            return response.Response('Detail:Not Enough Stock.',status=status.HTTP_400_BAD_REQUEST)
        
        order=Order.objects.create(user=user.id,product=product_id,quantity=quantity,status='CONFIRMED')
        reduce_inventory(product_id,quantity,token)
        return response.Response(OrderSerializer(order).data,status=status.HTTP_201_CREATED)
        
