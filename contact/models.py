from django.db import models


class Contact_model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    project_details = models.TextField()
# Create your models here.
