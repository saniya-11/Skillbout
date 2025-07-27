from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productDescription = models.TextField()

    def _str_(self):
        return self.ProductName