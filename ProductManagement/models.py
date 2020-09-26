from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='products/images/', blank=True, default="products/images/default.jpg")
    file = models.FileField(upload_to='products/files/', blank=True, null=True, default='products/files/default.pdf')

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)