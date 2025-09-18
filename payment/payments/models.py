from django.db import models

# Create your models here.
class Payment(models.Model):
    STATUS_CHOICES=[
        ('pending','PENDING'),
        ('success','SUCCESS'),
       ('failed','FAILED')
    ]
    user=models.IntegerField()
    order=models.IntegerField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment for order-id {self.order} - {self.status}'
