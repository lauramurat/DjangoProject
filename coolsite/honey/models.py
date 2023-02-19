from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
# Create your models here.
