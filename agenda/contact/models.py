from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=12, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=False, blank=False)
    email = models.EmailField()
    company = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(default=date.today)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
