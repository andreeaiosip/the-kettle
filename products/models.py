from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    strength = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/img')
    price = models.DecimalField(max_digits=6, decimal_places=2)


def __str__(self):
    return self.name


class Tea(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    tea_bags = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='static/img')
    price = models.DecimalField(max_digits=6, decimal_places=2)


def __str__(self):
    return self.name

