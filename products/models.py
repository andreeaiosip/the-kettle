from django.db import models

# Create your models here.


class Product(models.Model):

    TEA = 'Tea'
    COFFEE = 'Coffee'
    CATEGORY_CHOICES = [
        (TEA, 'Tea'),
        (COFFEE, 'Coffee'),
    ]
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='static/img')
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


