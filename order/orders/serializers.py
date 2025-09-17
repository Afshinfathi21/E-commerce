from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','product','user','quantity','status','created_at']
        read_only_fields=['id','user','status','created_at']
        