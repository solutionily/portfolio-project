from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)# Create your models here.
