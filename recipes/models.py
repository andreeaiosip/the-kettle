from django.db import models

# Create your models here.

class  Recipe(models.Model):

    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=20, null=True, blank=True)
    duration = 

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

