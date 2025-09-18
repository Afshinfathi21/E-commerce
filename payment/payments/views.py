from django.shortcuts import render
from rest_framework import permissions,viewsets,response,status
from .models import Payment
from .serializers import PaymentSerializer
from .utils import update_order
# Create your views here.

class PaymentView(viewsets.ModelViewSet):
    serializer_class=PaymentSerializer
    queryset=Payment.objects.all()
    permission_classes=[permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        token=self.request.headers.get('Authorization')
        if not token:
            return response.Response('error:no token provided.',status=status.HTTP_401_UNAUTHORIZED)
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment=serializer.save(user=request.user.id,status='pending')

        # payment here,after that if successfull we update order status
        success=True
        if success:
            payment.status='success'
            payment.save()

            if not update_order(token,payment.order):
                return response.Response('error:failed to notify order service.')
        
        else:
            payment.status='failed'
            payment.save()
        return response.Response(PaymentSerializer(payment).data,status=status.HTTP_201_CREATED)