from django.db import models

# Create your models here.
class Inbox(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    message = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Inbox'
        verbose_name_plural = 'Inbox'

def __str__(self):
    return self.name
