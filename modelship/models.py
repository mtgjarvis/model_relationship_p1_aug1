from django.db import models


class Customer(models.Model):
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Name: {self.name} Address: {self.address} Email: {self.email}'


class Order(models.Model):
    order_num = models.IntegerField()
    date = models.DateField()
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
