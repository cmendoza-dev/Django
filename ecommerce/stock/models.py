from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    short_description = models.TextField(blank=False, max_length=100, null=False)
    description = models.TextField(blank=False, null=False)
    stock = models.IntegerField(default=20)
    discount_until = models.DateField(default=date.today)

    def __str__(self):
        return self.name


