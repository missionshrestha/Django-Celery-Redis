from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100)
    pipeline = models.CharField(max_length=100)
    cluster = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    schedule = models.DateTimeField(auto_now_add=True) 
    description = models.TextField()