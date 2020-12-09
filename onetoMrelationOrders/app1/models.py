from django.db import models

# Create your models here.
class ProductModel(models.Model):
    pno=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    quantity=models.IntegerField()
    Photo=models.ImageField(upload_to='products/')

class CustomerModel(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)
    address=models.TextField(max_length=50)
    image=models.ImageField(upload_to='customer/')
    contact=models.IntegerField()
    password=models.IntegerField()

class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    orderdate = models.DateField(auto_now_add=True)
    Customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    Product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
