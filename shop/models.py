
from django.db import models


# Create your models here.
class  Customer(models.Model):
    name = models.CharField("Customer",max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    adress = models.CharField(max_length=300)
    contact = models.CharField(max_length=200)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Orders(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name='customer')
    product_id = models.CharField(max_length=6)
    quantity = models.CharField(max_length=3)
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.status
