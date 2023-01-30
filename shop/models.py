from tabnanny import verbose
from django.db import models

# Create your models here.
class  Customers(models.Model):
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