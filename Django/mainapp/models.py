from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    data_received = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=64)

    def __str__(self):
        return self.name
