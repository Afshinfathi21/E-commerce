from django.db import models

# Create your models here.


class Order(models.Model):
    Choices={
        'pending':'PENDING',
        'canceled':'CANCELED',
        'completed':'COMPLETED'
    }

    product=models.IntegerField()
    user=models.IntegerField()

    quantity=models.PositiveIntegerField(default=0)
    status=models.CharField(choices=Choices, max_length=9,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f'Order {self.id} - User {self.user} - Product {self.product} - '
    
