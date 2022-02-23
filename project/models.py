from django.db import models


class projectModel(models.Model):
    image = models.ImageField()
    For = models.CharField(max_length=50)
    project = models.TextField(max_length=500)

# Create your models here.
