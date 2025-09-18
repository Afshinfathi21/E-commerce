from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name