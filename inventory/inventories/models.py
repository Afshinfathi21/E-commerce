from django.db import models

# Create your models here.

class Inventory(models.Model):
    product=models.IntegerField(unique=True)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f'Product {self.product} - Qty {self.quantity}'