from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        app_label = 'Store'


class Slider(models.Model):
    name=models.CharField(max_length=255)
    photo = models.ImageField()
    description= models.CharField(max_length=255, blank=True, null=True)
    status=models.BooleanField(default=True)


class Logo(models.Model):
    photo = models.ImageField()

