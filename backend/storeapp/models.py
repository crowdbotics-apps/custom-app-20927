from django.conf import settings
from django.db import models


class Products(models.Model):
    "Generated Model"
    shoes = models.CharField(
        max_length=256,
    )


class Product(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    price = models.FloatField()
    image = models.URLField()


# Create your models here.
