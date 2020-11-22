from django.db import models

# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class Fruits(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class Colours(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


