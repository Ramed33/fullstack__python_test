from django.conf import settings
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    price = models.FloatField()