# models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.URLField()
    def __str__(self):
        return self.title
