from django.db import models


# Create your models here.

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    purpose = (models.CharField(max_length=100))
    created = models.DateTimeField(auto_now_add=True)
