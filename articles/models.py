from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

