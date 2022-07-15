from django.db import models

# Create your models here.
class Phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
