from django.db import models

# Create your models here.

class Book(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    path = models.TextField()