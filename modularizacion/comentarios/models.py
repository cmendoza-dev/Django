from django.db import models

# Create your models here.
class Comment(models.Model):

    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3, null=False)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=255, default='Firma')
    
    def __str__(self):
        return self.name

